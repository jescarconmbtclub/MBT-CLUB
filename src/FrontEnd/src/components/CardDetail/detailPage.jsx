import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './detailPage.css';
import { BASE_API_URL } from '../../constants';

const CardDetail = () => {
  const { codigo } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await axios.get(`${BASE_API_URL}/api/productos/producto/?codigo=${codigo}`);
        const filteredLists = response.data.filter(list => list.length > 0);
        const productData = filteredLists.length > 0 ? filteredLists[0][0] : null;
        setProduct(productData);
      } catch (error) {
        console.error('Error fetching product details:', error);
      }
    };

    fetchProduct();
  }, [codigo]);

  if (!product) {
    return <div>Loading...</div>;
  }

  // Determinar qué precio mostrar
  let precioToShow = product.precio;
  if (product.precio_rebajado && parseFloat(product.precio_rebajado) < parseFloat(product.precio)) {
    precioToShow = (
      <>
        <span className="rebajado">{product.precio_rebajado}</span>
        <span className="tachado">{product.precio}</span>
      </>
    );
  }

  return (
    <div className="detail-container">
      <div className="product-image-container">
        <img src={product.imagen_url} alt={product.nombre} className="product-image" />
      </div>
      <div className="product-details">
        <p className="product-name">Nombre: {product.nombre}</p>
        <p className="product-material">Material: {product.material}</p>
        <p className="product-price">Precio: {precioToShow}</p>
        <p className="product-description">Descripción: {product.descripcion}</p>
        <p className="product-measures">Medidas: {product.medidas}</p>
      </div>
    </div>
  );
};

export default CardDetail;
