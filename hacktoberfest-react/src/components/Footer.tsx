import { FaGithub, FaLinkedin, FaTwitter, FaFacebook, FaInstagram } from 'react-icons/fa';

const currentYear = new Date().getFullYear();

export default function Footer() {
  return (
    <footer className="bg-gray-900 text-white py-12">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center mb-4">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 300 300"
                className="w-10 h-10 text-hacktoberfest-pink mr-3"
              >
                <path
                  fill="currentColor"
                  d="M0.7,0.7v298.7h298.7V0.7H0.7z M197.8,271.4l-32-32v-95.6l-31.4,31.4v79l-17.3,17.3L99.8,254V70.4L95,65.6  L73,87.7L61.7,76.5l47.8-47.8l0.1,0.1l0,0l1.9,1.8l22.8,22.8V136l31.4-31.4V70.2L150,54.4l25.8-25.8l24.7,24.7v169.1l12.1,12.1  l14.7-14.7l11.1,11.1L197.8,271.4z"
                />
              </svg>
              <h2 className="text-2xl font-bold bg-gradient-to-r from-hacktoberfest-pink to-purple-500 bg-clip-text text-transparent">
                Hacktoberfest {currentYear}
              </h2>
            </div>
            <p className="text-gray-400 mb-4">
              This project is participating in Hacktoberfest. Join us in celebrating open source!
            </p>
            <div className="flex space-x-4 mt-4">
              <a href="https://github.com/fineanmol/Hacktoberfest2024" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">
                <FaGithub className="w-6 h-6" />
              </a>
              <a href="https://linkedin.com/in/fineanmol" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">
                <FaLinkedin className="w-6 h-6" />
              </a>
              <a href="https://twitter.com/fineanmol" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">
                <FaTwitter className="w-6 h-6" />
              </a>
              <a href="https://facebook.com/fineanmol" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">
                <FaFacebook className="w-6 h-6" />
              </a>
              <a href="https://instagram.com/fineanmol" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">
                <FaInstagram className="w-6 h-6" />
              </a>
            </div>
          </div>

          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li><a href="#home" className="text-gray-400 hover:text-white transition-colors">Home</a></li>
              <li><a href="#contributors" className="text-gray-400 hover:text-white transition-colors">Contributors</a></li>
              <li><a href="#about" className="text-gray-400 hover:text-white transition-colors">About</a></li>
              <li><a href="https://hacktoberfest.digitalocean.com/" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">Hacktoberfest</a></li>
            </ul>
          </div>

          <div>
            <h3 className="text-lg font-semibold mb-4">Resources</h3>
            <ul className="space-y-2">
              <li><a href="https://hacktoberfest.digitalocean.com/resources" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">Getting Started</a></li>
              <li><a href="https://github.com/fineanmol/Hacktoberfest2024" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">GitHub Repository</a></li>
              <li><a href="https://github.com/fineanmol/Hacktoberfest2024/issues" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">Open Issues</a></li>
              <li><a href="https://github.com/fineanmol/Hacktoberfest2024/pulls" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors">Pull Requests</a></li>
            </ul>
          </div>
        </div>

        <div className="border-t border-gray-800 mt-12 pt-8 text-center text-gray-500 text-sm">
          <p>© {currentYear} Hacktoberfest. All rights reserved. Made with ❤️ by the open source community.</p>
        </div>
      </div>
    </footer>
  );
}
