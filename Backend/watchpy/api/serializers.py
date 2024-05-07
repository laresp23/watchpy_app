# Serializadores de Django REST Framework
from rest_framework import serializers

# Modelo de usuario de Django
from django.contrib.auth.models import User

# Validadores de Django
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError  

# Serializador para el modelo de Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    # Campo de nombre de usuario
    username = serializers.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9.@_+-]+$',
                message='El nombre de usuario solo puede contener letras, dígitos y @/./+/-/_',
            ),
        ],
        error_messages={
            'required': 'El nombre de usuario es requerido.',
            'max_length': 'El nombre de usuario debe tener menos de 150 caracteres.',
        }
    )
    
    # Campo de contraseña
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
        error_messages={
            'required': 'La contraseña es requerida.',
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    # Valida que la contraseña no contenga partes del nombre de usuario o correo electrónico
    def validate(self, data):
        user = User(**data)
        password = data.get('password')
        if user.username.lower() in password.lower() or user.email.lower() in password.lower():
            raise serializers.ValidationError("La contraseña no puede contener partes del nombre de usuario o correo electrónico.")
        return data

    # Crea un nuevo usuario
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Serializador para datos de inicio de sesión
class LoginSerializer(serializers.Serializer):
    # Campo para nombre de usuario
    nombre_usuario = serializers.CharField()
    
    # Campo para contraseña
    contraseña = serializers.CharField(style={'input_type': 'password'})

# Serializador para datos de películas
class PeliculaSerializer(serializers.Serializer):
    # Campo para ID
    id = serializers.IntegerField()
    
    # Campo para título
    title = serializers.CharField()
    
    # Campo para descripción
    overview = serializers.CharField()
    
    # Campo para ruta del póster
    poster_path = serializers.CharField()
    
    # Campo para calificación
    vote_average = serializers.FloatField()

# Serializador para datos de series
class SerieSerializer(serializers.Serializer):
    # Campo para ID
    id = serializers.IntegerField()
    
    # Campo para nombre
    name = serializers.CharField()
    
    # Campo para descripción
    overview = serializers.CharField()
    
    # Campo para ruta del póster
    poster_path = serializers.CharField()
    
    # Campo para calificación
    vote_average = serializers.FloatField()
