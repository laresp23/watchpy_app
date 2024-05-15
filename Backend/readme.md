# API de Watch.PY

La API de Watch.PY es una plataforma de streaming que proporciona endpoints para obtener información sobre películas, series, usuarios y perfiles, así como para la autenticación de usuarios mediante tokens JWT. También integra datos de la API externa The Movie Database para ofrecer detalles y trailers de películas y series.

## Funcionalidades principales

- **Inicio:** Proporciona información sobre la API.
- **Documentación de la API:** Ofrece la documentación detallada de todos los endpoints de la API.
- **Obtener token de acceso:** Permite a los usuarios autenticados obtener un token de acceso JWT proporcionando sus credenciales de inicio de sesión.
- **Refrescar token de acceso:** Permite refrescar un token de acceso JWT expirado mediante la presentación de un token de actualización válido.
- **Verificar token de acceso:** Permite verificar la validez de un token de acceso JWT.
- **Listar películas y series:** Obtiene la lista de todas las películas y series disponibles en la API.
- **Listar películas y series populares:** Obtiene la lista de películas y series populares en la API.
- **Detalle de una película o serie:** Obtiene los detalles de una película o serie específica identificada por su clave primaria.
- **Registrar usuario:** Permite registrar un nuevo usuario en la API.
- **Iniciar sesión de usuario:** Permite a un usuario iniciar sesión en la API proporcionando sus credenciales de inicio de sesión.
- **Cerrar sesión de usuario:** Permite a un usuario cerrar sesión en la API, invalidando su token de acceso.
- **Listar usuarios:** Obtiene la lista de todos los usuarios registrados en la API.
- **Obtener, actualizar y eliminar un usuario específico:** Permite obtener, actualizar y eliminar usuarios específicos identificados por su id.
- **Listar y crear perfiles de usuario:** Permite listar todos los perfiles de usuario existentes y crear nuevos perfiles de usuario.
- **Obtener y actualizar el perfil de usuario:** Permite obtener y actualizar el perfil de usuario.

## Uso de la API

### Requisitos

- Python 3.x
- Django
- Django REST Framework
- Requests

### Instalación

1. Clona el repositorio:

    ```bash
    git clone git clone https://github.com/laresp23/watchpy_app.git
    ```

2. Instala el entorno virtual, las dependencias y abrimos la carpeta desde linea de comandos:

    ```bash
    python3 -m venv myenv
    myenv\Scripts\activate
    pip install -r requirements.txt
    cd watchpy
    ```

3. Ejecuta las migraciones:

    ```bash
    python manage.py makemigrations
    python manage.py makemigrations api
    ```

4. Aplica las migraciones:

    ```bash
    python manage.py migrate
    ```

5. Crea un superusuario:

    ```bash
    python manage.py createsuperuser
    ```

6. Recolecta los archivos estáticos:

    ```bash
    python manage.py collectstatic
    ```

7. Inicia el servidor:

    ```bash
    python manage.py runserver
    ```


### Documentación

Accede a la documentación de la API en http://localhost:8000/api/docs/.

### Endpoints principales

- **Inicio:** `/api/`
- **Documentación de la API:** `/api/docs/`
- **Obtener token de acceso:** `/api/token/`
- **Refrescar token de acceso:** `/api/token/refresh/`
- **Verificar token de acceso:** `/api/token/verify/`
- **Listar películas:** `/api/peliculas/`
- **Listar series:** `/api/series/`
- **Listar películas populares:** `/api/peliculas/populares/`
- **Listar series populares:** `/api/series/populares/`
- **Detalle de una película:** `/api/pelicula/<id>/`
- **Detalle de una serie:** `/api/serie/<id>/`
- **Registrar usuario:** `/api/registrar/`
- **Iniciar sesión de usuario:** `/api/iniciar-sesion/`
- **Cerrar sesión de usuario:** `/api/cerrar-sesion/`
- **Listar usuarios:** `/api/usuarios/`
- **Obtener, actualizar y eliminar un usuario específico:** `/api/usuarios/<id>/`
- **Listar y crear perfiles de usuario:** `/api/perfiles/`
- **Obtener y actualizar el perfil de usuario:** `/api/perfiles/<id>/`

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.