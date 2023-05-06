/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        gray: {
          100: 'rgba(83, 83, 83, 0.25)',
          200: 'rgba(255, 255, 255, 0.18)'
        }
      },
      fontFamily: {
        welbut: ['welbut', 'sans-serif']
      }
    },
  },
  plugins: [],
}

