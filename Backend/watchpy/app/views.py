from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

@require_http_methods(["GET"])
def home(request):
    """Renderiza la página de inicio."""
    return JsonResponse({"message": "Welcome to Watch.PY API"})

@require_http_methods(["GET"])
def peliculas(request):
    """Obtiene y muestra las películas populares."""
    movies = obtener_medios('movie')
    return JsonResponse({'movies': movies})

@require_http_methods(["GET"])
def series(request):
    """Obtiene y muestra las series populares."""
    series = obtener_medios('tv')
    return JsonResponse({'series': series})

@require_http_methods(["GET"])
def detalle_media(request):
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

@api_view(['POST'])
def register(request):
    """Registra un nuevo usuario."""
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Se requieren nombre de usuario y contraseña'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'El nombre de usuario ya está en uso'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    """Inicia sesión de un usuario."""
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_user(request):
    """Cierra sesión de un usuario."""
    logout(request)
    return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request, user_id):
    """Obtiene los detalles de un usuario."""
    try:
        user = User.objects.get(pk=user_id)
        return Response({'username': user.username}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_user(request, user_id):
    """Actualiza los detalles de un usuario."""
    try:
        user = User.objects.get(pk=user_id)
        username = request.data.get('username')
        if username:
            user.username = username
            user.save()
            return Response({'message': 'Usuario actualizado correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Nombre de usuario requerido'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user(request, user_id):
    """Elimina un usuario."""
    try:
        user = User.objects.get(pk=user_id)
        user.delete()
        return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

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

def obtener_api_key():
    """Obtiene la clave de la API (debería implementar una lógica más segura para obtenerla)."""
    return 'fe1a6340812a4559051b8ec620a4e866'
