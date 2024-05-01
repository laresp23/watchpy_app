# Watch.PY API

Esta API forma parte del backend para el proyecto de fin de ciclo de Desarrollo de Aplicaciones Web (DAW). Proporciona endpoints para acceder a información sobre películas y series, así como funcionalidades de autenticación de usuarios.

## Endpoints

### Home

- **URL:** `/`
- **Método:** GET
- **Descripción:** Renderiza la página de inicio.
- **Respuesta:** JSON con un mensaje de bienvenida.

### Películas

- **URL:** `/peliculas/`
- **Método:** GET
- **Descripción:** Obtiene y muestra las películas populares.
- **Respuesta:** JSON con la lista de películas populares.

### Series

- **URL:** `/series/`
- **Método:** GET
- **Descripción:** Obtiene y muestra las series populares.
- **Respuesta:** JSON con la lista de series populares.

### Detalle de medio

- **URL:** `/detalle-media/`
- **Método:** GET
- **Descripción:** Obtiene los detalles de una película o serie y su trailer.
- **Parámetros GET:**
  - `media_type`: tipo de medio ('movie' o 'tv').
  - `id`: ID de la película o serie.
- **Respuesta:** JSON con los detalles del medio y el trailer.

### Registro de usuario

- **URL:** `/register/`
- **Método:** POST
- **Descripción:** Registra un nuevo usuario.
- **Parámetros POST:** `username`, `password`.
- **Respuesta:** JSON con un mensaje de éxito o error.

### Inicio de sesión de usuario

- **URL:** `/login/`
- **Método:** POST
- **Descripción:** Inicia sesión de un usuario.
- **Parámetros POST:** `username`, `password`.
- **Respuesta:** JSON con un mensaje de éxito o error.

### Cierre de sesión de usuario

- **URL:** `/logout/`
- **Método:** POST
- **Descripción:** Cierra sesión de un usuario.
- **Respuesta:** JSON con un mensaje de éxito.

### Obtener usuario

- **URL:** `/user/<user_id>/`
- **Método:** GET
- **Descripción:** Obtiene los detalles de un usuario.
- **Respuesta:** JSON con el nombre de usuario o un mensaje de error.

### Actualizar usuario

- **URL:** `/user/<user_id>/`
- **Método:** PUT
- **Descripción:** Actualiza los detalles de un usuario.
- **Parámetros PUT:** `username`.
- **Respuesta:** JSON con un mensaje de éxito o error.

### Eliminar usuario

- **URL:** `/user/<user_id>/`
- **Método:** DELETE
- **Descripción:** Elimina un usuario.
- **Respuesta:** JSON con un mensaje de éxito o error.

## Recursos externos

La API utiliza la base de datos de The Movie Database (TMDb) para obtener información sobre películas y series.

## Requisitos

- Python 3.x
- Django
- Django Rest Framework
- Paquete `requests`

## Configuración

1. Clona este repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta las migraciones con `python manage.py migrate`.
4. Obtén una clave de API de The Movie Database y configúrala en la función `obtener_api_key()`.

## Uso

1. Ejecuta el servidor con `python manage.py runserver`.
2. Accede a los endpoints según sea necesario.

## Contribución

Si quieres contribuir a este proyecto, siéntete libre de abrir un *pull request*.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
