import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { register } from '../utils/api';

function Register() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    try {
      if (password !== confirmPassword) {
        throw new Error('Las contraseñas no coinciden');
      }
      await register(username, password, email);
      navigate('/login'); 
    } catch (error) {
      setError(error.message);
    }
    setLoading(false);
  };

  return (
    <div className="bg-gray-900 text-white flex flex-col min-h-screen">
      <Navbar />
      <div className="flex-grow bg-jumbotron">
        <div className="container mx-auto px-4 py-16">
          <div className="max-w-md mx-auto bg-gray-800 p-8 rounded-lg shadow-lg">
            <h2 className="text-3xl font-bold text-center mb-8">Regístrate</h2>
            <form onSubmit={handleSubmit}>
              <div className="mb-4">
                <label htmlFor="username" className="block text-white mb-2">Nombre de usuario</label>
                <input 
                  type="text" 
                  id="username" 
                  name="username" 
                  className="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:border-blue-500" 
                  value={username} 
                  onChange={(e) => setUsername(e.target.value)} 
                  required 
                />
              </div>
              <div className="mb-4">
                <label htmlFor="email" className="block text-white mb-2">Correo electrónico</label>
                <input 
                  type="email" 
                  id="email" 
                  name="email" 
                  className="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:border-blue-500" 
                  value={email} 
                  onChange={(e) => setEmail(e.target.value)} 
                  required 
                />
              </div>
              <div className="mb-4">
                <label htmlFor="password" className="block text-white mb-2">Contraseña</label>
                <input 
                  type="password" 
                  id="password" 
                  name="password" 
                  className="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:border-blue-500" 
                  value={password} 
                  onChange={(e) => setPassword(e.target.value)} 
                  required 
                />
              </div>
              <div className="mb-4">
                <label htmlFor="confirmPassword" className="block text-white mb-2">Confirmar contraseña</label>
                <input 
                  type="password" 
                  id="confirmPassword" 
                  name="confirmPassword" 
                  className="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:border-blue-500" 
                  value={confirmPassword} 
                  onChange={(e) => setConfirmPassword(e.target.value)} 
                  required 
                />
              </div>
              <div className="mb-6">
                <button 
                  type="submit" 
                  className={`w-full bg-green-500 text-white py-3 rounded-lg font-semibold text-lg hover:bg-green-600 transition duration-300 ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
                  disabled={loading}
                >
                  {loading ? 'Cargando...' : 'Registrarse'}
                </button>
              </div>
              {error && <p className="text-red-500 text-center">{error}</p>}
            </form>
            <p className="text-center text-gray-400 text-sm">¿Ya tienes una cuenta? <Link to="/login" className="text-blue-500">Inicia sesión</Link></p>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Register;
