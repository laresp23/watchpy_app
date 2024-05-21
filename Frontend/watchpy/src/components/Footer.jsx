import React from 'react';
import '../assets/css/Footer.css'

function Footer() {
  return (
    <>
    <footer className="footer bg-footer text-footer">
        <div className="container mx-auto px-4 py-8 text-center">
            <p>© 2024 WatchPY</p>
            <ul className="flex justify-center mt-4">
                <li className="mr-6"><a href="#" className="text-white">Términos de servicio</a></li>
                <li className="mr-6"><a href="#" className="text-white">Política de privacidad</a></li>
                <li><a href="#" className="text-white">Contacto</a></li>
            </ul>
        </div>
    </footer>
    </>
  );
}

export default Footer;
