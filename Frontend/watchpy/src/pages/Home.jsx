import React, { useEffect, useState } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { getPeliculas, getSeries } from '../utils/api';
import MovieList from '../components/MovieList';
import SerieList from '../components/SerieList';

const Home = () => {
  const [peliculas, setPeliculas] = useState([]);
  const [series, setSeries] = useState([]);
  const [loadingPeliculas, setLoadingPeliculas] = useState(true);
  const [loadingSeries, setLoadingSeries] = useState(true);
  const [errorPeliculas, setErrorPeliculas] = useState(null); 
  const [errorSeries, setErrorSeries] = useState(null); 
  
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

  return (
    <div className="bg-gray-900 text-white flex flex-col min-h-screen">
      <Navbar />
      <div className="flex-grow p-8 mt-16">
        {loadingPeliculas ? (
          <p>Cargando películas...</p>
        ) : errorPeliculas ? (
          <p>{errorPeliculas}</p>
        ) : (
          <MovieList peliculas={peliculas} />
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
      
      <Footer />
    </div>
  );
};

export default Home;
