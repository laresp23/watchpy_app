from django.test import TestCase
from django.contrib.auth.models import User
from .models import Media, Trailer, UserProfile

class MediaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configura datos de prueba para Media
        Media.objects.create(
            title='Interstellar',
            overview='Un equipo de exploradores viaja a través de un agujero de gusano en el espacio en un intento por garantizar la supervivencia de la humanidad.',
            poster_path='/abc123.jpg',
            media_type='movie'
        )

    def test_title_content(self):
        # Verifica que el título del medio sea correcto
        media = Media.objects.get(id=1)
        expected_object_name = f'{media.title}'
        self.assertEquals(expected_object_name, 'Interstellar')

    def test_media_type_content(self):
        # Verifica que el tipo de medio sea correcto
        media = Media.objects.get(id=1)
        expected_object_name = f'{media.media_type}'
        self.assertEquals(expected_object_name, 'movie')

    # Agrega más pruebas para otros campos si es necesario

class TrailerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configura datos de prueba para Trailer
        media = Media.objects.create(
            title='Inception',
            overview='Un ladrón que roba secretos corporativos a través del uso de la tecnología de intercambio de sueños recibe la tarea inversa de plantar una idea en la mente de un CEO.',
            poster_path='/xyz456.jpg',
            media_type='movie'
        )
        Trailer.objects.create(media=media, key='xyz789')

    def test_key_content(self):
        # Verifica que la clave del tráiler sea correcta
        trailer = Trailer.objects.get(id=1)
        expected_object_name = f'{trailer.key}'
        self.assertEquals(expected_object_name, 'xyz789')

    # Agrega más pruebas si es necesario

class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configura datos de prueba para UserProfile
        user = User.objects.create_user(username='testuser', password='12345')
        UserProfile.objects.create(user=user, bio='Esta es una biografía de prueba.', birth_date='2000-01-01')

    def test_bio_content(self):
        # Verifica que el contenido de la biografía sea correcto
        profile = UserProfile.objects.get(id=1)
        expected_object_name = f'{profile.bio}'
        self.assertEquals(expected_object_name, 'Esta es una biografía de prueba.')

    # Agrega más pruebas si es necesario
