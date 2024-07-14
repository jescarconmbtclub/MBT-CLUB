import React from 'react';
import './Navbar.css';

export default function Navbar() {
  return (
      <div className="navbar-container">
          <div className="navbar">
            <div className="navbar-pages">
                <div><a href="#">Metal</a></div>
                <div><a href="#">Madera</a></div>
                <div><a href="#">Cuero</a></div>
                <div><a href="#">PLA</a></div>
                <div><a href="#">Goma Eva</a></div>
                <div><a href="#">Cerámica</a></div>
                <div><a href="#">Cristal</a></div>
                <div><a href="#">Tejido</a></div>
                <div><a href="#">Espuma</a></div>
            </div>
            <div className="navbar-auth">
              <a href="#">Inicia Sesión</a>
            </div>
          </div>
      </div>
  );
}
