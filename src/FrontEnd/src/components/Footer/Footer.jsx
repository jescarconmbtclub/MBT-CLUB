import React from 'react';
import './footer.css';

export default function Footer() {
  return (
    <div className='Footer-container'>
      <div className='Footer'>
        <div className='Footer-contact'>
          <div><a href='#'>Sobre Nosotros</a></div>
          <div><br></br></div>
          <div><a href='#'>Contacto</a></div>
        </div>
        <div className='Footer-redes'>
          <div><a href='https://www.instagram.com/mbt.club?igsh=MXVpZDhoZHg3ajMx'>Instagram</a></div>
          <div><a href='https://www.youtube.com/@mbt-club'>Youtube</a></div> 
          <div><a href='https://www.tiktok.com/@mbt.club?_t=8o1ToAa6gF7&_r=1'>TikTok</a></div>
        </div>
      </div>
    </div>
    
  );
}
