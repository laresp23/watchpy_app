import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

const axiosInstance = axios.create({
  baseURL: API_URL,
});

const TOKEN_KEY = 'access_token';

// Función para establecer el token JWT en el encabezado de autorización de las solicitudes
const setAuthToken = (token) => {
  if (token) {
    axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    sessionStorage.setItem(TOKEN_KEY, token); // Guardar el token en sessionStorage
  } else {
    delete axiosInstance.defaults.headers.common['Authorization'];
    sessionStorage.removeItem(TOKEN_KEY); // Eliminar el token de sessionStorage
  }
};

// Función para obtener el token JWT del almacenamiento de sesión
const getAuthToken = () => {
  return sessionStorage.getItem(TOKEN_KEY); // Obtener el token de sessionStorage
};

// Verificar si hay un token guardado al cargar la página y establecerlo en las solicitudes
const token = getAuthToken();
if (token) {
  setAuthToken(token);
}

export const login = async (username, password) => {
  try {
    const response = await axiosInstance.post('/iniciar-sesion/', { username, password });
    const { access_token, username: loggedInUsername, email } = response.data;

    // Guardar los datos del usuario en sessionStorage
    sessionStorage.setItem('username', loggedInUsername);
    sessionStorage.setItem('email', email);

    // Establecer el token de acceso en sessionStorage
    setAuthToken(access_token);

    return response.data;
  } catch (error) {
    console.error('Axios error:', error);
    throw error;
  }
};

export const register = async (username, password, email) => {
  try {
    const response = await axiosInstance.post('/registrar/', { username, password, email });
    return response.data;
  } catch (error) {
    console.error('Axios error:', error);
    throw error;
  }
};

export const getPeliculas = async () => {
  try {
    const response = await axiosInstance.get('/peliculas/');
    return response.data.peliculas;
  } catch (error) {
    console.error('Axios error:', error);
    throw error;
  }
};

export const getPeliculasFavoritas = async () => {
  try {
    const response = await axiosInstance.get('/peliculas-populares/');
    return response.data.peliculas_populares;
  } catch (error) {
    console.error('Axios error:', error);
    throw error;
  }
};

export const getSeries = async () => {
  try {
    const response = await axiosInstance.get('/series/');
    return response.data.series;
  } catch (error) {
    console.error('Axios error:', error);
    throw error;
  }
};

export const getSeriesFavoritas = async () => {
  try {
    const response = await axiosInstance.get('/series-populares/');
    return response.data.series_populares;
  } catch (error) {
    console.error('Axios error:', error);
    throw error;
  }
};

export default axiosInstance;
