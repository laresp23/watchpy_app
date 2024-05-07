# Modelo de usuario de Django para autenticación y gestión de usuarios
from django.contrib.auth.models import User

# Funciones relacionadas con la autenticación
from django.contrib.auth import authenticate, login, logout

# Funciones de acceso rápido para obtener objetos o generar un error 404
from django.shortcuts import get_object_or_404

# Vistas y ViewSets para puntos finales de la API
from rest_framework.views import APIView

# Clase de respuesta para devolver respuestas de la API
from rest_framework.response import Response

# Códigos de estado HTTP
from rest_framework import status

# Clases de permisos para controlar el acceso a las vistas
from rest_framework.permissions import IsAuthenticated

# Decorador para establecer permisos en las vistas
from rest_framework.decorators import api_view, permission_classes

# Función de reversión para generar URLs
from rest_framework.reverse import reverse

# Generación de tokens y autenticación
from rest_framework_simplejwt.tokens import RefreshToken

# Importación de serializadores para serialización/deserialización de datos
from .serializers import (
    UsuarioSerializer,  # Serializador para datos de usuario
    LoginSerializer,    # Serializador para datos de inicio de sesión
    PeliculaSerializer, # Serializador para datos de películas
    SerieSerializer,    # Serializador para datos de series
)
from rest_framework.permissions import AllowAny

# Solicitudes externas
import requests


# Constantes
API_KEY = "fe1a6340812a4559051b8ec620a4e866"
IDIOMA = "es"


# Funciones de utilidad
def obtener_medios(tipo_medio):
    """Obtiene los medios (películas o series) populares."""
    url = f"https://api.themoviedb.org/3/{tipo_medio}/popular?api_key={API_KEY}&language={IDIOMA}"
    response = requests.get(url)
    data = response.json().get("results", [])
    return data


def obtener_detalles(tipo_medio, id_item):
    """Obtiene los detalles de una película o serie."""
    url = f"https://api.themoviedb.org/3/{tipo_medio}/{id_item}?api_key={API_KEY}&language={IDIOMA}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def obtener_trailer(tipo_medio, id_item):
    """Obtiene el trailer de una película o serie."""
    url = f"https://api.themoviedb.org/3/{tipo_medio}/{id_item}/videos?api_key={API_KEY}&language={IDIOMA}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("results"):
            return data["results"][0].get("key")
    return None

# Funciones de utilidad para el manejo de usuarios
def username_existente(username):
    return User.objects.filter(username__iexact=username).exists()

def email_existente(email):
    return User.objects.filter(email__iexact=email).exists()

def validar_usuario(username, email):
    if username_existente(username):
        raise ValueError("El nombre de usuario ya está en uso.")
    if email_existente(email):
        raise ValueError("El correo electrónico ya está en uso.")

# Funciones Api
class Home(APIView):
    """Renderiza la página de inicio."""

    def get(self, request):
        return Response({"message": "Bienvenido a la API de Watch.PY"})


class Peliculas(APIView):
    """Obtiene y muestra las películas populares."""

    def get(self, request):
        peliculas = obtener_medios("movie")
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response({"peliculas": serializer.data})


class Series(APIView):
    """Obtiene y muestra las series populares."""

    def get(self, request):
        series = obtener_medios("tv")
        serializer = SerieSerializer(series, many=True)
        return Response({"series": serializer.data})


class DetallePelicula(APIView):
    """Obtiene los detalles de una película y su trailer."""

    def get(self, request, pk):
        detalles_pelicula = obtener_detalles("movie", pk)
        if not detalles_pelicula:
            return Response(
                {"error": "No se encontró la película"},
                status=status.HTTP_404_NOT_FOUND,
            )

        trailer_key = obtener_trailer("movie", pk)
        return Response(
            {"detalles_media": detalles_pelicula, "trailer_key": trailer_key}
        )


class DetalleSerie(APIView):
    """Obtiene los detalles de una serie y su trailer."""

    def get(self, request, pk):
        detalles_serie = obtener_detalles("tv", pk)
        if not detalles_serie:
            return Response(
                {"error": "No se encontró la serie"}, status=status.HTTP_404_NOT_FOUND
            )

        trailer_key = obtener_trailer("tv", pk)
        return Response({"detalles_media": detalles_serie, "trailer_key": trailer_key})


class RegistrarUsuario(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')

            try:
                validar_usuario(username, email)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({"message": "Registro completo"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IniciarSesionUsuario(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        nombre_usuario = serializer.validated_data["nombre_usuario"]
        contraseña = serializer.validated_data["contraseña"]

        usuario = authenticate(username=nombre_usuario, password=contraseña)
        if not usuario:
            return Response(
                {"message": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        login(request, usuario)
        refresh = RefreshToken.for_user(usuario)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})

class CerrarSesionUsuario(APIView):
    """Cierra sesión de usuario."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            {"message": "Sesión cerrada correctamente"}, status=status.HTTP_200_OK
        )


class ListaUsuarios(APIView):
    """Obtiene la lista de usuarios."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuarios = User.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)


class DetalleUsuario(APIView):
    """Obtiene, actualiza o elimina un usuario."""

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        usuario = get_object_or_404(User, pk=pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk):
        usuario = get_object_or_404(User, pk=pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        usuario = get_object_or_404(User, pk=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def raiz_api(request, format=None):
    """Obtiene la lista de endpoints de la API."""
    if request.method == "GET":
        return Response(
            {
                "inicio": reverse("home", request=request, format=format),
                "peliculas": reverse("peliculas", request=request, format=format),
                "series": reverse("series", request=request, format=format),
                "detalle_media": reverse(
                    "detalle-media", request=request, format=format
                ),
                "registrar": reverse("registrar", request=request, format=format),
                "iniciar_sesion": reverse(
                    "iniciar-sesion", request=request, format=format
                ),
                "cerrar_sesion": reverse(
                    "cerrar-sesion", request=request, format=format
                ),
                "usuarios": reverse("lista-usuarios", request=request, format=format),
            }
        )


@api_view(["GET"])
def no_encontrado(request, exception=None):
    """Maneja errores 404."""
    return Response({"error": "Página no encontrada"}, status=status.HTTP_404_NOT_FOUND)
