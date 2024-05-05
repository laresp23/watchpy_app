from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.reverse import reverse as api_reverse
from rest_framework_simplejwt.tokens import RefreshToken
from .models import WatchedMedia, Movie, Serie
from .serializers import UserSerializer, LoginSerializer
import requests

# Obtener películas, series y detalles

def obtener_api_key():
    """Obtiene la clave de la API (debería implementar una lógica más segura para obtenerla)."""
    return 'fe1a6340812a4559051b8ec620a4e866'

def obtener_medios(media_type):
    """Obtiene los medios (películas o series) populares."""
    api_key = obtener_api_key()
    language = 'es'
    url = f'https://api.themoviedb.org/3/{media_type}/popular?api_key={api_key}&language={language}'
    response = requests.get(url)
    data = response.json().get('results', [])
    return data

def obtener_detalles(media_type, item_id):
    """
    Obtiene los detalles de una película o serie.
    
    Parámetros GET:
    - media_type: tipo de medio ('movie' o 'tv').
    - id: ID de la película o serie.
    """
    api_key = obtener_api_key()
    language = 'es'
    url = f'https://api.themoviedb.org/3/{media_type}/{item_id}?api_key={api_key}&language={language}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def obtener_trailer(media_type, item_id):
    """
    Obtiene el trailer de una película o serie.
    
    Parámetros GET:
    - media_type: tipo de medio ('movie' o 'tv').
    - id: ID de la película o serie.
    """
    api_key = obtener_api_key()
    language = 'es'
    url = f'https://api.themoviedb.org/3/{media_type}/{item_id}/videos?api_key={api_key}&language={language}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get('results'):
            return data['results'][0].get('key')
    return None

def not_found(request, exception=None):
    return Response({"error": "Página no encontrada"}, status=status.HTTP_404_NOT_FOUND)

class Home(APIView):
    @staticmethod
    def get(request):
        """Renderiza la página de inicio."""
        return JsonResponse({"message": "Welcome to Watch.PY API"})

class Peliculas(APIView):
    @staticmethod
    def get(request):
        """Obtiene y muestra las películas populares."""
        movies = obtener_medios('movie')
        return JsonResponse({'movies': movies})

class Series(APIView):
    @staticmethod
    def get(request):
        """Obtiene y muestra las series populares."""
        series = obtener_medios('tv')
        return JsonResponse({'series': series})

class DetalleMedia(APIView):
    @staticmethod
    def get(request):
        """
        Obtiene los detalles de una película o serie y su trailer.
        
        Parámetros GET:
        - media_type: tipo de medio ('movie' o 'tv').
        - id: ID de la película o serie.
        """
        media_type = request.GET.get('media_type')
        item_id = request.GET.get('id')
        
        if media_type in ['movie', 'tv'] and item_id.isdigit():
            media_details = obtener_detalles(media_type, item_id)
            trailer_key = obtener_trailer(media_type, item_id)
            return JsonResponse({'media_details': media_details, 'trailer_key': trailer_key})
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)

class RegisterUser(APIView):
    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registro completo"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    @staticmethod
    @require_http_methods(["POST"])
    def post(request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"message": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)  # Aquí se realiza el login del usuario
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })

class LogoutUser(APIView):
    @staticmethod
    def post(request):
        logout(request)
        return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'home': api_reverse('home', request=request, format=format),
        'peliculas': api_reverse('peliculas', request=request, format=format),
        'series': api_reverse('series', request=request, format=format),
        'detalle_media': api_reverse('detalle-media', request=request, format=format),
        'register': api_reverse('register', request=request, format=format),
        'login': api_reverse('login', request=request, format=format),
        'logout': api_reverse('logout', request=request, format=format),
        'users': api_reverse('user-list', request=request, format=format)
    })

@api_view(['POST'])
def mark_movie_as_watched(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    
    # Verificar si el usuario ya ha visto esta película
    if not WatchedMedia.objects.filter(user=user, media=movie).exists():
        # Si no, crear instancia de WatchedMedia
        watched_movie = WatchedMedia.objects.create(user=user, media=movie)
        return Response({"message": "Película marcada como vista"}, status=status.HTTP_201_CREATED)
    else:
        # Si el usuario ya ha visto la película, devolver un mensaje de error
        return Response({"error": "El usuario ya ha marcado esta película como vista"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def mark_series_as_watched(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    user = request.user
    
    # Verificar si el usuario ya ha visto esta serie
    if not WatchedMedia.objects.filter(user=user, media=series).exists():
        # Si no, crear instancia de WatchedMedia
        watched_series = WatchedMedia.objects.create(user=user, media=series)
        return Response({"message": "Serie marcada como vista"}, status=status.HTTP_201_CREATED)
    else:
        # Si el usuario ya ha visto la serie, devolver un mensaje de error
        return Response({"error": "El usuario ya ha marcado esta serie como vista"}, status=status.HTTP_400_BAD_REQUEST)