import React from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

const MovieList = ({ peliculas }) => {
  const settings = {
    dots: false,
    infinite: true,
    speed: 500,
    slidesToShow: 4,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: false
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          initialSlide: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  };

  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">Películas</h2>
      {peliculas && peliculas.length > 0 ? (
        <Slider {...settings}>
          {peliculas.map((pelicula) => (
            <div key={pelicula.id} className="relative">
              <div className="w-64 h-36">
                <img className="w-full h-full object-cover" src={`https://image.tmdb.org/t/p/w300${pelicula.poster_path}`} alt={pelicula.title} />
              </div>
              <div className="absolute bottom-0 left-0 w-full bg-gradient-to-t from-black to-transparent p-4">
                <h3 className="text-white font-bold text-lg">{pelicula.title}</h3>
              </div>
            </div>
          ))}
        </Slider>
      ) : (
        <p>No hay películas disponibles</p>
      )}
    </div>
  );
};

export default MovieList;
