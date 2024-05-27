import React from 'react';

const SerieCard = ({ serie }) => {
  return (
    <div className="movie-card">
      <h3>{serie.name}</h3>
      <p>{serie.overview}</p>
      <img src={`https://image.tmdb.org/t/p/w500${serie.poster_path}`} alt={serie.name} />
    </div>
  );
};

export default SerieCard;
