from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
 
from .serializers import (
    UsuarioSerializer,
    LoginSerializer,
    PeliculaSerializer,
    SerieSerializer,
)
import requests

# Clave de API de The Movie Database
API_KEY = "fe1a6340812a4559051b8ec620a4e866"
IDIOMA = "es"

# Vista para la página de inicio de la API
class Home(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Bienvenido a la API de Watch.PY"})

# Vista para obtener películas
class Peliculas(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        peliculas = obtener_medios("movie")
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response({"peliculas": serializer.data})

# Vista para obtener series
class Series(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        series = obtener_medios("tv")
        serializer = SerieSerializer(series, many=True)
        return Response({"series": serializer.data})


# Vista para obtener películas populares
class PeliculasPopulares(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        peliculas = obtener_medios_populares("movie")
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response({"peliculas_populares": serializer.data})

# Vista para obtener series populares
class SeriesPopulares(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        series = obtener_medios_populares("tv")
        serializer = SerieSerializer(series, many=True)
        return Response({"series_populares": serializer.data})

# Vista para obtener detalles de una película
class DetallePelicula(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        detalles_pelicula = obtener_detalles("movie", pk)
        if not detalles_pelicula:
            return Response({"error": "No se encontró la película"}, status=status.HTTP_404_NOT_FOUND)

        trailer_key = obtener_trailer("movie", pk)
        return Response({"detalles_media": detalles_pelicula, "trailer_key": trailer_key})

# Vista para obtener detalles de una serie
class DetalleSerie(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        detalles_serie = obtener_detalles("tv", pk)
        if not detalles_serie:
            return Response({"error": "No se encontró la serie"}, status=status.HTTP_404_NOT_FOUND)

        trailer_key = obtener_trailer("tv", pk)
        return Response({"detalles_media": detalles_serie, "trailer_key": trailer_key})

# Vista para registrar un nuevo usuario
class RegistrarUsuario(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Usuario registrado correctamente",
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para iniciar sesión de un usuario
class IniciarSesionUsuario(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Inicio de sesión exitoso",
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para cerrar sesión de un usuario
class CerrarSesionUsuario(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')

            if not refresh_token:
                return Response({"error": "Se requiere el campo 'refresh_token'."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()
            BlacklistedToken.objects.create(token=refresh_token)

            return Response({"message": "Sesión cerrada exitosamente."}, status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Vista para obtener la lista de usuarios
class ListaUsuarios(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuarios = User.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

# Vista para obtener detalles, actualizar o eliminar un usuario específico
class DetalleUsuario(APIView):
    authentication_classes = [JWTAuthentication]
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

# Vista para obtener y actualizar el perfil de usuario
class PerfilUsuarioAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        perfiles = User.objects.filter(id=request.user.id)
        serializer = UsuarioSerializer(perfiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(User=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, perfil_id):
        perfil = get_object_or_404(User, pk=perfil_id, id=request.user.id)
        serializer = UsuarioSerializer(perfil, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, perfil_id):
        perfil = get_object_or_404(User, pk=perfil_id, id=request.user.id)
        perfil.delete()
        return Response({"message": "Perfil eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

# Función para obtener una lista de medios (películas o series) según el tipo especificado.
def obtener_medios(tipo_medio):
    url = f"https://api.themoviedb.org/3/discover/{tipo_medio}?api_key={API_KEY}&language={IDIOMA}&sort_by=title.asc"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json().get("results", [])
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return []

# Función para obtener una lista de medios (películas o series) populares según el tipo especificado.
def obtener_medios_populares(tipo_medio):
    url = f"https://api.themoviedb.org/3/{tipo_medio}/popular?api_key={API_KEY}&language={IDIOMA}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json().get("results", [])
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return []

# Función para obtener los detalles de un medio específico (película o serie).
def obtener_detalles(tipo_medio, id_item):
    url = f"https://api.themoviedb.org/3/{tipo_medio}/{id_item}?api_key={API_KEY}&language={IDIOMA}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

# Función para obtener el trailer de un medio específico (película o serie).
def obtener_trailer(tipo_medio, id_item):
    url = f"https://api.themoviedb.org/3/{tipo_medio}/{id_item}/videos?api_key={API_KEY}&language={IDIOMA}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("results"):
            return data["results"][0].get("key")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

# Función para verificar si un nombre de usuario ya existe
def username_existente(username):
    return User.objects.filter(username__iexact=username).exists()

# Función para verificar si un correo electrónico ya existe
def email_existente(email):
    return User.objects.filter(email__iexact=email).exists()

# Función para validar si un nombre de usuario o correo electrónico ya están en uso
def validar_usuario(username, email):
    if username_existente(username):
        raise ValueError("El nombre de usuario ya está en uso.")
    if email_existente(email):
        raise ValueError("El correo electrónico ya está en uso.")
    
# Vista para obtener la URL raíz de la API y sus endpoints
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def raiz_api(request, format=None):
    if request.method == "GET":
        return Response({
            "inicio": reverse("home", request=request, format=format),
            "peliculas": reverse("peliculas", request=request, format=format),
            "series": reverse("series", request=request, format=format),
            "peliculas_populares": reverse("peliculas-populares", request=request, format=format),
            "series_populares": reverse("series-populares", request=request, format=format),
            "detalle_media": reverse("detalle-media", request=request, format=format),
            "registrar": reverse("registrar", request=request, format=format),
            "iniciar_sesion": reverse("iniciar-sesion", request=request, format=format),
            "cerrar_sesion": reverse("cerrar-sesion", request=request, format=format),
            "usuarios": reverse("lista-usuarios", request=request, format=format),
            "perfiles_usuario": reverse("perfil-usuario-list", request=request, format=format),
            "token_obtener": reverse("token_obtain_pair", request=request, format=format),
            "token_refrescar": reverse("token_refresh", request=request, format=format),
            "token_verificar": reverse("token_verify", request=request, format=format),
        })

# Vista para manejar una página no encontrada (error 404)
@api_view(["GET"])
def no_encontrado(request, exception=None):
    return render(request, '404.html', status=status.HTTP_404_NOT_FOUND)

# Vistas personalizadas para obtener, refrescar y verificar tokens JWT
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

class CustomTokenVerifyView(TokenVerifyView):
    permission_classes = [AllowAny]