import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './navbar.css';

export default function Navbar() {
  const location = useLocation();

  return (
    <div className="navbar-container">
      <div className="navbar">
        <div className="navbar-pages">
          <div><Link to="/productos/material/metal" className={location.pathname === '/productos/material/metal' ? 'active' : ''}>Metal</Link></div>
          <div><Link to="/productos/material/madera" className={location.pathname === '/productos/material/madera' ? 'active' : ''}>Madera</Link></div>
          <div><Link to="/productos/material/cuero" className={location.pathname === '/productos/material/cuero' ? 'active' : ''}>Cuero</Link></div>
          <div><Link to="/productos/material/ceramica" className={location.pathname === '/productos/material/ceramica' ? 'active' : ''}>Cerámica</Link></div>
          <div><Link to="/productos/material/cristal" className={location.pathname === '/productos/material/cristal' ? 'active' : ''}>Cristal</Link></div>
          <div><Link to="/productos/material/tejido" className={location.pathname === '/productos/material/tejido' ? 'active' : ''}>Tejido</Link></div>
          <div className="dropdown">
            <span>Plásticos</span>
            <div className="dropdown-content">
              <div><Link to="/productos/material/pla">PLA</Link></div>
              <div><Link to="/productos/material/goma-eva">Goma Eva</Link></div>
              <div><Link to="/productos/material/espuma">Espuma</Link></div>
            </div>
          </div>        
        </div>
        <div className="navbar-auth">
          <Link to="#" className={location.pathname === '#' ? 'active' : ''}>Inicia Sesión</Link>
        </div>
      </div>
    </div>
  );
}
