import React from 'react';
import { Link } from 'react-router-dom';
import './navbar.css';

export default function Navbar() {
  return (
    <div className="navbar-container">
      <div className="navbar">
        <div className="navbar-pages">
          <div><Link to="/productos/metal">Metal</Link></div>
          <div><Link to="/productos/madera">Madera</Link></div>
          <div><Link to="/productos/cuero">Cuero</Link></div>
          <div><Link to="/productos/pla">PLA</Link></div>
          <div><Link to="/productos/goma-eva">Goma Eva</Link></div>
          <div><Link to="/productos/ceramica">Cerámica</Link></div>
          <div><Link to="/productos/cristal">Cristal</Link></div>
          <div><Link to="/productos/tejido">Tejido</Link></div>
          <div><Link to="/productos/espuma">Espuma</Link></div>
        </div>
        <div className="navbar-auth">
          <Link to="#">Inicia Sesión</Link>
        </div>
      </div>
    </div>
  );
}
