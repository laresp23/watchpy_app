import React from 'react';

const MovieCard = ({ pelicula }) => {
  return (
    <div className="movie-card">
      <h3>{pelicula.title}</h3>
      <p>{pelicula.overview}</p>
      <img src={`https://image.tmdb.org/t/p/w500${pelicula.poster_path}`} alt={pelicula.title} />
    </div>
  );
};

export default MovieCard;
