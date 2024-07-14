import React from 'react';
import './home.css';

export default function Home() {
  return (
    <div className="home-container">
      <div className="video-container">
        <video controls controlsList="nodownload" className='video'>
          <source src="/videos/VideoIntro.mp4" type="video/mp4" />
          {/* Agrega más sources según los formatos de video que desees soportar */}
          Tu navegador no soporta el elemento de video.
        </video>
      </div>
    </div>
  );
}
