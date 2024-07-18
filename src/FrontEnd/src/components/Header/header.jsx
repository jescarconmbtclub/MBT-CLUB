import React from 'react';
import { Link } from 'react-router-dom';
import './header.css';

const logoUrl = "/imgs/Banner-logo.png"; // Variable para la URL de la imagen

export default function Header() {
  return (
    <div className='Header-container'>          
        <Link to="/" className="header-link">
            <div className='header-logo'>
              <img src={logoUrl} alt="Logo" className="logo-img" />
            </div>
            <div className="header-text">
                <h1 className="title">MBT Club</h1>
                <h2 className="subtitle">Si puedes imaginarlo, podemos hacerlo.</h2>
            </div>
        </Link>
    </div>
  );
}
