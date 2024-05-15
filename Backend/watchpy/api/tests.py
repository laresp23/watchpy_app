from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import PerfilUsuario, Pelicula, Serie 

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Crear usuarios de prueba
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.user = PerfilUsuario.objects.create_user(**self.user_data)

        # Crear películas y series de prueba
        self.pelicula = Pelicula.objects.create(titulo='Test Movie', director='Director Test')
        self.serie = Serie.objects.create(titulo='Test Series', creador='Creador Test')

    def test_api_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_peliculas(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('peliculas'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_series(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('series'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_peliculas_populares(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('peliculas_populares'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_series_populares(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('series_populares'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_detalle_pelicula(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('detalle_pelicula', args=[self.pelicula.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_detalle_serie(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('detalle_serie', args=[self.serie.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_registro_usuario(self):
        response = self.client.post(reverse('registrar_usuario'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_inicio_sesion_usuario(self):
        response = self.client.post(reverse('iniciar_sesion_usuario'), {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
