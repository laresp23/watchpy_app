# WatchPy - Aplicación para Ver Películas y Series

WatchPy es una aplicación desarrollada con React y Vite que te permite explorar una amplia colección de películas y series. Utilizando tecnologías modernas, ofrece una experiencia fluida y rápida de navegación. 

## Características Principales

- **Exploración de Contenido:** Permite a los usuarios explorar una amplia variedad de películas y series.
- **Autenticación de Usuarios:** Funcionalidad de inicio de sesión y registro para una experiencia personalizada.
- **Diseño Responsivo:** Adaptado para proporcionar una experiencia óptima en dispositivos móviles y de escritorio.
- **Gestión de Errores:** Manejo eficiente de errores para una experiencia de usuario sin problemas.
- **Integración de API:** Utiliza Axios para gestionar las solicitudes a la API backend.

## Configuración

1. Clonar el Repositorio:

   ```bash
   git clone git clone https://github.com/laresp23/watchpy_app.git
   ```

2. Instalar Dependencias: 

   ```bash
   cd Frontend
   cd watchpy
   npm install
   ```

3. Iniciar el Servidor de Desarrollo:

   ```bash
   npm run dev
   ```

4. Visitar [http://localhost:3000](http://localhost:3000) en el navegador para acceder a la aplicación.

## Uso

- **Inicio de Sesión:** Accede a la página de inicio de sesión (`/login`) para iniciar sesión con tu nombre de usuario y contraseña.
- **Registro:** Si eres nuevo, puedes registrarte visitando `/register`.
- **Exploración:** Después de iniciar sesión, serás redirigido a la página principal donde podrás explorar y disfrutar de películas y series.

## Estructura de Carpetas

- **/src/components:** Contiene componentes reutilizables en toda la aplicación.
- **/src/pages:** Incluye las diferentes páginas de la aplicación, como Inicio de Sesión, Registro, y la Página Principal.
- **/src/utils:** Contiene funciones de utilidad y lógica de integración de la API.
- **/src/index.css:** Estilos globales para la aplicación.
- **/src/App.jsx:** Componente raíz para el enrutamiento.

## Dependencias

- React
- Vite
- React Router DOM
- Axios
- Tailwind CSS

## Endpoints de la API

- `/api/login`: Endpoint para iniciar sesión de usuario.
- `/api/register`: Endpoint para registro de usuario.
- `/api/peliculas`: Endpoint para obtener películas.
- `/api/series`: Endpoint para obtener series.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
