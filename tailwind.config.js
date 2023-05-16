/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        gray: {
          100: 'rgba(83, 83, 83, 0.25)',
          200: 'rgba(255, 255, 255, 0.20)',
        },
        darkblue: {
          600: '#000814',
          400: '#001d3d',
          200: '#003566'
        }
      },
      fontFamily: {
        welbut: ['welbut', 'sans-serif'],
        univers: ['univers', 'sans-serif']
      }
    },
    screens: {
      'sm': '300px',
      // => @media (min-width: 640px) { ... }

      'md': '600px',
      // => @media (min-width: 768px) { ... }

      'lg': '1024px',
      // => @media (min-width: 1024px) { ... }

      'xl': '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1536px',
      // => @media (min-width: 1536px) { ... }
    }
  },
  plugins: [],
}

