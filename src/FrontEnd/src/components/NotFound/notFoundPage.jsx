import React from 'react';
import './notFoundPage.css';

export default function NotFound() {
  return (
    <div className="not-found">
      <h1 className="not-found-title">Error #404</h1>
      <p className="not-found-message">¡Oh no! El sitio que buscas no se encuentra en este reino.</p>
    </div>
  );
}
