/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'hacktoberfest-pink': '#FF0844',
        'hacktoberfest-purple': '#6f42c1',
        'hacktoberfest-dark': '#1a1a2e',
      },
      fontFamily: {
        'special-elite': ['"Special Elite"', 'cursive'],
      },
      animation: {
        'rubber-band': 'rubberBand 1s',
      },
      keyframes: {
        rubberBand: {
          '0%, 100%': { transform: 'scale(1)' },
          '30%': { transform: 'scaleX(1.25) scaleY(0.75)' },
          '40%': { transform: 'scaleX(0.75) scaleY(1.25)' },
          '60%': { transform: 'scaleX(1.15) scaleY(0.85)' },
          '80%': { transform: 'scaleX(0.95) scaleY(1.05)' },
        }
      }
    },
  },
  plugins: [],
}
