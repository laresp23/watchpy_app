import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../components/NavbarProfile';
import Footer from '../components/Footer';

const Profiles = () => {
  return (
    <div className="bg-gray-900 text-white flex flex-col min-h-screen">
      <Navbar />
      <div className="flex-grow bg-jumbotron">
        {/* Botón para acceder a /home */}
      <div className="flex justify-center py-4">
        <Link to="/home" className="bg-blue-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition duration-300">Ir a Home</Link>
      </div>
        <div className="container mx-auto px-4 py-16 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-8">
            
          {/* Formulario para crear nuevo perfil */}
          <div className="md:col-span-2 bg-gray-800 p-4 rounded-lg shadow-lg">
            <h2 className="text-3xl font-bold text-center mb-8">Crear nuevo perfil</h2>
            <form id="newProfileForm">
              <div className="mb-4">
                <label htmlFor="profileName" className="block text-white mb-2">Nombre del perfil</label>
                <input type="text" id="profileName" name="profileName"
                  className="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:border-blue-500"
                  required
                />
              </div>
              <div className="mb-6">
                <button type="submit" className="w-full bg-green-600 text-white py-3 rounded-lg font-semibold text-lg hover:bg-green-700 transition duration-300">
                  Crear perfil
                </button>
              </div>
            </form>
          </div>
          {/* Tarjetas de perfiles */}
          <div className="md:col-span-3 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">
            {/* Perfil 1 */}
            <div className="bg-gray-800 p-4 rounded-lg shadow-lg flex flex-col justify-between">
              <div>
                <h3 className="text-xl font-bold mb-2">Perfil 1</h3>
                {/* Otra información del perfil */}
              </div>
              <div className="flex justify-between mt-4">
                <button className="bg-blue-500 text-white px-4 py-2 rounded-lg font-semibold">Actualizar</button>
                <button className="bg-red-500 text-white px-4 py-2 rounded-lg font-semibold">Borrar</button>
              </div>
            </div>
            {/* Perfil 2 */}
            <div className="bg-gray-800 p-4 rounded-lg shadow-lg flex flex-col justify-between">
              <div>
                <h3 className="text-xl font-bold mb-2">Perfil 2</h3>
                {/* Otra información del perfil */}
              </div>
              <div className="flex justify-between mt-4">
                <button className="bg-blue-500 text-white px-4 py-2 rounded-lg font-semibold">Actualizar</button>
                <button className="bg-red-500 text-white px-4 py-2 rounded-lg font-semibold">Borrar</button>
              </div>
            </div>
            {/* Perfil 3 */}
            <div className="bg-gray-800 p-4 rounded-lg shadow-lg flex flex-col justify-between">
              <div>
                <h3 className="text-xl font-bold mb-2">Perfil 3</h3>
                {/* Otra información del perfil */}
              </div>
              <div className="flex justify-between mt-4">
                <button className="bg-blue-500 text-white px-4 py-2 rounded-lg font-semibold">Actualizar</button>
                <button className="bg-red-500 text-white px-4 py-2 rounded-lg font-semibold">Borrar</button>
              </div>
            </div>
            {/* Perfil 4 */}
            <div className="bg-gray-800 p-4 rounded-lg shadow-lg flex flex-col justify-between">
              <div>
                <h3 className="text-xl font-bold mb-2">Perfil 4</h3>
                {/* Otra información del perfil */}
              </div>
              <div className="flex justify-between mt-4">
                <button className="bg-blue-500 text-white px-4 py-2 rounded-lg font-semibold">Actualizar</button>
                <button className="bg-red-500 text-white px-4 py-2 rounded-lg font-semibold">Borrar</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <Footer />
      
    </div>
  );
};

export default Profiles;
