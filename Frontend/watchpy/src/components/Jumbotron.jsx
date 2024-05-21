import React from 'react';
import { Link } from 'react-router-dom';
import '../assets/css/Jumbotron.css'

function Jumbotron() {
  return (
    <>
    <div className="jumbotron bg-jumbotron bg-cover bg-center flex items-center justify-center text-center relative">
            <div className="absolute inset-0 bg-black opacity-50" />
            <div className="container mx-auto px-4 py-16 relative z-10">
                <h1 className="text-5xl font-bold mb-8 text-jumbotron">Bienvenido a WatchPY</h1>
                <p className="text-xl mb-8 text-jumbotron">Disfruta de miles de películas y series en cualquier lugar, sin
                    compromiso.</p>
                    <Link to="/register"  className="btn-get-started bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-8 rounded-full uppercase transition duration-300 md:block">Comienza
                    ahora</Link>
            </div>
        </div>
    </>
  );
}

export default Jumbotron;
