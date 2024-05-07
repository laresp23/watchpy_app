# Serializadores de Django REST Framework
from rest_framework import serializers

# Modelo de usuario de Django
from django.contrib.auth.models import User

# Serializador para el modelo de Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Serializador para datos de inicio de sesión
class LoginSerializer(serializers.Serializer):
    nombre_usuario = serializers.CharField()
    contraseña = serializers.CharField(style={'input_type': 'password'})

# Serializador para datos de películas
class PeliculaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    overview = serializers.CharField()
    poster_path = serializers.CharField()
    vote_average = serializers.FloatField()

# Serializador para datos de series
class SerieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    overview = serializers.CharField()
    poster_path = serializers.CharField()
    vote_average = serializers.FloatField()
