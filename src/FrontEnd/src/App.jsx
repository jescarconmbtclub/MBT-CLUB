import React, { useState } from 'react';
import { BrowserRouter, Routes, Route, Link,useLocation,Navigate } from "react-router-dom";
import './App.css';
import Navbar from './components/Navbar/navbar';
import Footer from './components/Footer/footer';
import Home from './components/Home/homePage';
import CardList from './components/CardList/cards';
import CardDetail from './components/CardDetail/detailPage';
import NotFound from './components/NotFound/notFoundPage';


const App = () => {
  return (
      <BrowserRouter>
        <div className="app-container">
          <Link to="/" className="header-link">
            <div className="header">
              <h1 className="title">MBT Club</h1>
              <h2 className="subtitle">Si puedes imaginarlo, podemos hacerlo.</h2>
            </div>
          </Link>
          <Navbar/>
          <MainContent />
          <div className='footer'><Footer/></div>
        </div>
       
      </BrowserRouter>
  );
};

const MainContent = () => {
  const location = useLocation();
  const [filtrosSeleccionados, setFiltrosSeleccionados] = useState({}); // Estado para almacenar filtros seleccionados

  // Función para aplicar filtros desde el componente Filter
  const aplicarFiltros = (filtros) => {
    setFiltrosSeleccionados(filtros);
  };


  return (
    <div className="main-content">
      <div>
        <Routes>
          <Route path="/" element={<Home/>} /> 
          <Route path="/productos/material/:material" element={<CardList/>} />
          <Route path="/productos/producto/:codigo" element={<CardDetail/>} />
          
          <Route path="*" element={<NotFound/>}/>
          {/*<Route path="/clothes/:tipo_prenda/" element={<Cloth_type_filter />} />
          <Route path="/clothes-details/:id/" element={<Cloth_details />} />

          <Route path="/login" element={<Login/>} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/register" element={<RegisterAndLogout />} />

          <Route path="/home" element={<Welcome />} />
          <Route path="/about-us" element={<AboutUs />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/brands" element={<Brand />} />
          <Route path="/brands/:marca/" element={<BrandClothes />} />
          <Route path="/blog" element={<Blog />} />
          <Route path="/blog/:id/" element={<Article_details />} />
          <Route path="/sales" element={<Sales />} />
          <Route path="/news" element={<News />} />
          <Route path="/search" element={<Search_bar />} /> 
          <Route path="*" element={<NotFound/>}></Route>*/}
        </Routes>
      </div>
    </div>
  );
};

export default App;
