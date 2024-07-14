import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './cards.css';
import { BASE_API_URL } from "../../constants";

const CardList = () => {
  const [products, setProducts] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage] = useState(8); // Cambia el número de productos por página según sea necesario
  const { material } = useParams();

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get(`${BASE_API_URL}/api/productos/material/?material=${material}`);
        setProducts(response.data.filter(productList => productList.length > 0)); // Filtra listas vacías
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, [material]);

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = products.slice(indexOfFirstItem, indexOfLastItem);

  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  // Mostrar mensaje cuando no hay productos y ocultar paginación
  if (products.length === 0) {
    return (
      <div className="cardList-container">
        <div className="no-products-message">
          <h3>Aún no disponemos de productos en esta sección.</h3>
          <p>Disculpa las molestias.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="cardList-container">
      <div className="products-list">
        {currentItems.map((productList, index) => (
          <div key={index} className="product-group">
            {productList.map(product => (
              <div key={product.id} className="product">
                <img src={product.imagen_url} alt={product.nombre} className="product-image" />
              </div>
            ))}
          </div>
        ))}
      </div>

      <div className="pagination">
        <button onClick={() => paginate(currentPage - 1)} disabled={currentPage === 1}>Anterior</button>
        <span>{` Página ${currentPage} de ${Math.ceil(products.length / itemsPerPage)} `}</span>
        <button onClick={() => paginate(currentPage + 1)} disabled={currentPage === Math.ceil(products.length / itemsPerPage)}>Siguiente</button>
      </div>
    </div>
  );
};

export default CardList;
