import React, { useEffect, useState } from 'react';
import Navbar from '../components/NavbarHome';
import Footer from '../components/Footer';
import { getPeliculas, getPeliculasFavoritas, getSeries, getSeriesFavoritas } from '../utils/api';
import MovieList from '../components/MovieList';
import MovieListFav from '../components/MovieListFav'; 
import SerieList from '../components/SerieList';
import SerieListFav from '../components/SerieListFav';

const Home = () => {
  const [peliculas, setPeliculas] = useState([]);
  const [peliculasFav, setPeliculasFav] = useState([]);
  const [series, setSeries] = useState([]);
  const [seriesFav, setSeriesFav] = useState([]);
  const [loadingPeliculas, setLoadingPeliculas] = useState(true);
  const [loadingPeliculasFav, setLoadingPeliculasFav] = useState(true);
  const [loadingSeries, setLoadingSeries] = useState(true);
  const [loadingSeriesFav, setLoadingSeriesFav] = useState(true);
  const [errorPeliculas, setErrorPeliculas] = useState(null);
  const [errorPeliculasFav, setErrorPeliculasFav] = useState(null);
  const [errorSeries, setErrorSeries] = useState(null);
  const [errorSeriesFav, setErrorSeriesFav] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const peliculasData = await getPeliculas();
        setPeliculas(peliculasData);
        setLoadingPeliculas(false);
      } catch (error) {
        setErrorPeliculas('Error al obtener las películas');
        setLoadingPeliculas(false);
        console.error('Error al obtener las películas:', error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const peliculasFavData = await getPeliculasFavoritas();
        setPeliculasFav(peliculasFavData);
        setLoadingPeliculasFav(false);
      } catch (error) {
        setErrorPeliculasFav('Error al obtener las películas Favoritas');
        setLoadingPeliculasFav(false);
        console.error('Error al obtener las películas:', error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const seriesData = await getSeries();
        setSeries(seriesData);
        setLoadingSeries(false);
      } catch (error) {
        setErrorSeries('Error al obtener las series');
        setLoadingSeries(false);
        console.error('Error al obtener las series:', error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const seriesFavData = await getSeriesFavoritas();
        setSeriesFav(seriesFavData);
        setLoadingSeriesFav(false);
      } catch (error) {
        setErrorSeriesFav('Error al obtener las series Favoritas');
        setLoadingSeriesFav(false);
        console.error('Error al obtener las series:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="bg-gray-900 text-white flex flex-col min-h-screen">
      <Navbar />
      <div className="p-8 mt-16">
        {loadingPeliculas ? (
          <p>Cargando películas...</p>
        ) : errorPeliculas ? (
          <p>{errorPeliculas}</p>
        ) : (
          <MovieList peliculas={peliculas} />
        )}
      </div>
      <div className="p-8">
        {loadingPeliculasFav ? (
          <p>Cargando películas favoritas...</p>
        ) : errorPeliculasFav ? (
          <p>{errorPeliculasFav}</p>
        ) : (
          <MovieListFav peliculasFav={peliculasFav} />
        )}
      </div>
      <div className="flex-grow p-8 ">
        {loadingSeries ? (
          <p>Cargando series...</p>
        ) : errorSeries ? (
          <p>{errorSeries}</p>
        ) : (
          <SerieList series={series} />
        )}
      </div>
      <div className="p-8 ">
        {loadingSeriesFav ? (
          <p>Cargando series favoritas...</p>
        ) : errorSeriesFav ? (
          <p>{errorSeriesFav}</p>
        ) : (
          <SerieListFav seriesFav={seriesFav} />
        )}
      </div>
      <Footer />
    </div>
  );
};

export default Home;
