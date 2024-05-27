import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import logo from '/logo.png';
import '../assets/css/Navbar.css'

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleNavbar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="bg-navbar p-4 absolute w-full z-10">
      <div className="container mx-auto flex flex-wrap items-center justify-between">
        <Link to="/" className="text-2xl font-bold flex items-center">
          <img src={logo} alt="Logo" className="h-8 mr-2" />
        </Link>
        <button
          onClick={toggleNavbar}
          className="navbar-toggler md:hidden focus:outline-none"
          aria-label="Abrir menú"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-6 w-6 text-white"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16m-7 6h7" />
          </svg>
        </button>
        {/* Menú para pantallas grandes */}
        <div className="hidden md:flex md:items-center md:w-auto w-full" id="navbarNavLarge">
          <div className="md:flex-grow md:flex md:justify-end">
            <div className="flex flex-col md:flex-row md:space-x-4 md:items-center ">
              <Link to="/profile" className="text-lg focus:outline-none mx-auto p-2">Editar Perfil</Link>
              <Link to="/logout" className="text-lg focus:outline-none mx-auto p-2">Cerrar Sesión</Link>
            </div>
          </div>
        </div>

        {/* Menú desplegable */}
        <div className={`md:hidden ${isOpen ? 'block' : 'hidden'} w-full `} id="navbarNavSmall">
          <div className="flex flex-col md:flex-row md:space-x-4 md:items-center justify-center">
            <Link to="/profile" className="text-lg focus:outline-none mx-auto p-2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-8 uppercase transition duration-300">Editar Perfil</Link>
          </div>
          <div className="flex flex-col md:flex-row md:space-x-4 md:items-center justify-center mt-4">
            <Link to="/logout" className="text-lg focus:outline-none mx-auto p-2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-8 uppercase transition duration-300">Cerrar Sesión</Link>
          </div>
        </div>
        
      </div>
    </nav>
  );
}

export default Navbar;
