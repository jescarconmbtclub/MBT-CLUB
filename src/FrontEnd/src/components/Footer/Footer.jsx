import React from 'react'
import './Footer.css'

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
                <div><a href='#'>Instagram</a></div>
                <div><a href='#'>Youtube</a></div> 
                <div><a href='#'>TikTok</a></div>
            </div>
        </div>
    </div>
  )
}
