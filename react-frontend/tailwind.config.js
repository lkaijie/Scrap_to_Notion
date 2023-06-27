/** @type {import('tailwindcss').Config} */
export default {
  mode: 'jit',
  content: [
    "./index.html",
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      gridTemplateColumns: {
        // Simple 16 column grid
        '16': 'repeat(16, minmax(0, 1fr))',

        // Complex site-specific column configuration
        'chart-big': '2fr 1fr',
      }
    },
  },
  plugins: [],
  darkMode:'class'

}

