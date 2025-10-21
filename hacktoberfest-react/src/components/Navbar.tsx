import { useState, useEffect } from 'react';
import { FaGithub, FaLinkedin, FaTwitter } from 'react-icons/fa';

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 10) {
        setIsScrolled(true);
      } else {
        setIsScrolled(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <nav className={`fixed w-full z-50 transition-all duration-300 ${
      isScrolled ? 'bg-gray-900/90 backdrop-blur-md py-2 shadow-lg' : 'bg-transparent py-4'
    }`}>
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <a href="/" className="flex items-center">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 300 300"
                className="w-10 h-10 text-hacktoberfest-pink"
              >
                <path
                  fill="currentColor"
                  d="M0.7,0.7v298.7h298.7V0.7H0.7z M197.8,271.4l-32-32v-95.6l-31.4,31.4v79l-17.3,17.3L99.8,254V70.4L95,65.6  L73,87.7L61.7,76.5l47.8-47.8l0.1,0.1l0,0l1.9,1.8l22.8,22.8V136l31.4-31.4V70.2L150,54.4l25.8-25.8l24.7,24.7v169.1l12.1,12.1  l14.7-14.7l11.1,11.1L197.8,271.4z"
                />
              </svg>
              <span className="ml-2 text-xl font-bold bg-gradient-to-r from-hacktoberfest-pink to-purple-500 bg-clip-text text-transparent">
                Hacktoberfest 2024
              </span>
            </a>
          </div>

          <div className="hidden md:flex items-center space-x-6">
            <a href="#home" className="text-gray-300 hover:text-white transition-colors">Home</a>
            <a href="#contributors" className="text-gray-300 hover:text-white transition-colors">Contributors</a>
            <a href="#about" className="text-gray-300 hover:text-white transition-colors">About</a>
            <div className="flex space-x-4 ml-4">
              <a href="https://github.com/fineanmol/Hacktoberfest2024" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">
                <FaGithub className="w-5 h-5" />
              </a>
              <a href="https://linkedin.com/in/fineanmol" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">
                <FaLinkedin className="w-5 h-5" />
              </a>
              <a href="https://twitter.com/fineanmol" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">
                <FaTwitter className="w-5 h-5" />
              </a>
            </div>
          </div>

          <button className="md:hidden text-gray-300 hover:text-white focus:outline-none">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>
    </nav>
  );
}
