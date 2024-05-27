import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Index from './pages/Index';
import Login from './pages/Login';
import Register from './pages/Register.jsx';
import Home from './pages/Home.jsx';
import Profiles from './pages/Profiles.jsx';


import './index.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Index />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/home" element={<Home />} />
        <Route path="/profiles" element={<Profiles />} />
      </Routes>
    </Router>
  );
}

export default App;
