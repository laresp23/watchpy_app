from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Pelicula, Serie
from rest_framework_simplejwt.tokens import RefreshToken


class UsuarioSerializer(serializers.ModelSerializer):
    """Serializador para el modelo de usuario."""

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """Crea un nuevo usuario."""
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        return user
   
class LoginSerializer(serializers.Serializer):
    """Serializador para datos de inicio de sesión."""

    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    def validate(self, data):
        """Valida las credenciales de inicio de sesión."""
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Credenciales inválidas.")

            data['user'] = user
        else:
            raise serializers.ValidationError("Se requiere nombre de usuario y contraseña.")

        return data

class PeliculaSerializer(serializers.ModelSerializer):
    """Serializador para datos de películas."""

    class Meta:
        model = Pelicula
        fields = ['id', 'title', 'overview', 'release_date', 'poster_path', 'vote_average']


class SerieSerializer(serializers.ModelSerializer):
    """Serializador para datos de series."""

    class Meta:
        model = Serie
        fields = ['id', 'name', 'overview', 'release_date', 'poster_path', 'vote_average']
