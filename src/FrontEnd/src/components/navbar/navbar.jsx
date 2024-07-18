

import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './navbar.css';

const logoUrl = "/imgs/navbar.png"; // Cambia esto a la ruta de tu imagen

export default function Navbar() {
  const location = useLocation();
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <div className="navbar-container">
      <div className="navbar">
        <div className="menu-icon" onClick={toggleMenu}>
          <img src={logoUrl} alt="Menu" />
        </div>
        <div className={`navbar-pages ${menuOpen ? 'open' : ''}`}>
          <div><Link to="/productos/material/metal" className={location.pathname === '/productos/material/metal' ? 'active' : ''}>Metal</Link></div>
          <div><Link to="/productos/material/madera" className={location.pathname === '/productos/material/madera' ? 'active' : ''}>Madera</Link></div>
          <div><Link to="/productos/material/cuero" className={location.pathname === '/productos/material/cuero' ? 'active' : ''}>Cuero</Link></div>
          <div><Link to="/productos/material/ceramica" className={location.pathname === '/productos/material/ceramica' ? 'active' : ''}>Cerámica</Link></div>
          <div><Link to="/productos/material/cristal" className={location.pathname === '/productos/material/cristal' ? 'active' : ''}>Cristal</Link></div>
          <div><Link to="/productos/material/tejido" className={location.pathname === '/productos/material/tejido' ? 'active' : ''}>Tejido</Link></div>
          <div><Link to="/productos/drops" className={location.pathname === '/productos/drops' ? 'active' : ''}>Drops</Link></div>
          <div><Link to="/productos/stickers" className={location.pathname === '/productos/stickers' ? 'active' : ''}>Stickers</Link></div>
          <div className="dropdown">
            <div>Plásticos</div>
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
