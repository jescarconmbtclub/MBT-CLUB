import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './navbar.css';

export default function Navbar() {
  const location = useLocation();
  
  return (
    <div className="navbar-container">
      <div className="navbar">
        <div className="navbar-pages">
          <div><Link to="/productos/material/metal" className={location.pathname === '/productos/metal' ? 'active' : ''}>Metal</Link></div>
          <div><Link to="/productos/material/madera" className={location.pathname === '/productos/madera' ? 'active' : ''}>Madera</Link></div>
          <div><Link to="/productos/material/cuero" className={location.pathname === '/productos/cuero' ? 'active' : ''}>Cuero</Link></div>
          <div><Link to="/productos/material/pla" className={location.pathname === '/productos/pla' ? 'active' : ''}>PLA</Link></div>
          <div><Link to="/productos/material/goma-eva" className={location.pathname === '/productos/goma-eva' ? 'active' : ''}>Goma Eva</Link></div>
          <div><Link to="/productos/material/ceramica" className={location.pathname === '/productos/ceramica' ? 'active' : ''}>Cerámica</Link></div>
          <div><Link to="/productos/material/cristal" className={location.pathname === '/productos/cristal' ? 'active' : ''}>Cristal</Link></div>
          <div><Link to="/productos/material/tejido" className={location.pathname === '/productos/tejido' ? 'active' : ''}>Tejido</Link></div>
          <div><Link to="/productos/material/espuma" className={location.pathname === '/productos/espuma' ? 'active' : ''}>Espuma</Link></div>
        </div>
        <div className="navbar-auth">
          <Link to="#" className={location.pathname === '#' ? 'active' : ''}>Inicia Sesión</Link>
        </div>
      </div>
    </div>
  );
}
