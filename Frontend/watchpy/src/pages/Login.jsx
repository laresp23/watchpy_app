import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { login } from '../utils/api';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    try {
      await login(username, password);
      navigate('/profiles');
    } catch (error) {
      setError(error.message || 'Hubo un problema con el inicio de sesión.');
    }
    setLoading(false);
  };

  return (
    <div className="bg-gray-900 text-white flex flex-col min-h-screen">
      <Navbar />
      <div className="flex-grow bg-jumbotron">
        <div className="container mx-auto px-4 py-16">
          <div className="max-w-md mx-auto bg-gray-800 p-8 rounded-lg shadow-lg">
            <h2 className="text-3xl font-bold text-center mb-8">Iniciar sesión</h2>
            <form onSubmit={handleSubmit}>
              <div className="mb-4">
                <label htmlFor="username" className="block text-white mb-2">Nombre de usuario</label>
                <input
                  type="text"
                  id="username"
                  name="username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:border-blue-500"
                  required
                />
              </div>
              <div className="mb-6">
                <label htmlFor="password" className="block text-white mb-2">Contraseña</label>
                <input
                  type="password"
                  id="password"
                  name="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:border-blue-500"
                  required
                />
              </div>
              <div className="mb-6">
                <button
                  type="submit"
                  className={`w-full bg-red-600 text-white py-3 rounded-lg font-semibold text-lg hover:bg-red-700 transition duration-300 ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
                  disabled={loading}
                >
                  {loading ? 'Cargando...' : 'Iniciar sesión'}
                </button>
              </div>
              {error && <p className="text-red-500 text-center">{error}</p>}
            </form>
            <p className="text-center text-gray-400 text-sm">¿No tienes una cuenta? <Link to="/register" className="text-blue-500">Regístrate</Link></p>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Login;
