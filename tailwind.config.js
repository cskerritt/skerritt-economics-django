/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './main/templates/**/*.html',
    './blog/templates/**/*.html',
    './tools/templates/**/*.html',
    './calculator/templates/**/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        // Custom colors for branding
        'sec-blue': '#2563eb',
        'sec-dark': '#1e293b',
        'sec-light': '#f8fafc',
      },
      fontFamily: {
        'sans': ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('daisyui'),
  ],
  daisyui: {
    themes: [
      {
        skerritt: {
          "primary": "#2563eb",
          "secondary": "#64748b",
          "accent": "#10b981",
          "neutral": "#1e293b",
          "base-100": "#ffffff",
          "info": "#3b82f6",
          "success": "#10b981",
          "warning": "#f59e0b",
          "error": "#ef4444",
        },
      },
      "light",
      "corporate",
    ],
    darkTheme: false,
    base: true,
    styled: true,
    utils: true,
    logs: false,
  },
}