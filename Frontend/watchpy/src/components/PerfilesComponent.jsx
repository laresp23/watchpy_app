import React from 'react';

const PerfilesComponent = ({ nombre }) => {
  return (
    <div className="bg-gray-800 p-4 rounded-lg shadow-lg flex flex-col justify-between">
      <div>
        <h3 className="text-xl font-bold mb-2">{nombre}</h3>
        {/* Otra información del perfil */}
      </div>
      <div className="flex justify-between mt-4">
        <button className="bg-blue-500 text-white px-4 py-2 rounded-lg font-semibold">Actualizar</button>
        <button className="bg-red-500 text-white px-4 py-2 rounded-lg font-semibold">Borrar</button>
      </div>
    </div>
  );
};

export default PerfilesComponent;
