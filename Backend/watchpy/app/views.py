# views.py

from django.shortcuts import render
import requests

def home(request):

    return render(request, 'app/home.html')

def peliculas(request):
    movies = obtener_medios('movie')
    return render(request, 'app/peliculas.html', {'movies': movies})

def series(request):
    series = obtener_medios('tv')
    return render(request, 'app/series.html', {'series': series})

def detalle_media(request):
    media_type = request.GET.get('media_type')
    item_id = request.GET.get('id')
    
    if media_type in ['movie', 'tv'] and item_id.isdigit():
        media_details = obtener_detalles(media_type, item_id)
        trailer_key = obtener_trailer(media_type, item_id)
        return render(request, 'app/detalle_media.html', {'media_details': media_details, 'trailer_key': trailer_key})
    else:
        return render(request, 'error.html')

def obtener_medios(media_type):
    api_key = obtener_api_key()
    language = 'es'
    url = f'https://api.themoviedb.org/3/{media_type}/popular?api_key={api_key}&language={language}'
    response = requests.get(url)
    data = response.json().get('results', [])
    return data

def obtener_detalles(media_type, item_id):
    api_key = obtener_api_key()
    language = 'es'
    url = f'https://api.themoviedb.org/3/{media_type}/{item_id}?api_key={api_key}&language={language}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def obtener_trailer(media_type, item_id):
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
    # Aquí puedes implementar la lógica para obtener la clave de API desde un archivo de configuración
    return 'fe1a6340812a4559051b8ec620a4e866'
