/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{ts,tsx,js,jsx}",
    "../Retail/frontend/**/*.{ts,tsx,js,jsx}",
    "../Core/frontend/**/*.{ts,tsx,js,jsx}",
    "../HRM/frontend/**/*.{ts,tsx,js,jsx}",
    "../CRM/frontend/**/*.{ts,tsx,js,jsx}",
    "../FMS/frontend/**/*.{ts,tsx,js,jsx}",
    "../Meet/frontend/**/*.{ts,tsx,js,jsx}",
    "../Common/frontend/**/*.{ts,tsx,js,jsx}"
  ],
  theme: {
    extend: {
      colors: {
        // Nexus Design System - Sophisticated & Modern
        nexus: {
          // Primary Brand Colors
          primary: {
            50: '#f0f4ff',
            100: '#e0e9ff',
            200: '#c7d6fe',
            300: '#a5b8fc',
            400: '#8b93f8',
            500: '#7c6df2',
            600: '#6d4de6',
            700: '#5d3dcb',
            800: '#4c32a4',
            900: '#402d82',
            950: '#261b4f',
          },

          // Neutral Grays - Warm undertones
          gray: {
            50: '#fafafa',
            100: '#f5f5f5',
            200: '#eeeeee',
            300: '#e0e0e0',
            400: '#bdbdbd',
            500: '#9e9e9e',
            600: '#757575',
            700: '#616161',
            800: '#424242',
            900: '#212121',
            950: '#0f0f0f',
          },

          // Success - Emerald inspired
          success: {
            50: '#ecfdf5',
            100: '#d1fae5',
            200: '#a7f3d0',
            300: '#6ee7b7',
            400: '#34d399',
            500: '#10b981',
            600: '#059669',
            700: '#047857',
            800: '#065f46',
            900: '#064e3b',
          },

          // Warning - Amber inspired
          warning: {
            50: '#fffbeb',
            100: '#fef3c7',
            200: '#fde68a',
            300: '#fcd34d',
            400: '#fbbf24',
            500: '#f59e0b',
            600: '#d97706',
            700: '#b45309',
            800: '#92400e',
            900: '#78350f',
          },

          // Error - Rose inspired
          error: {
            50: '#fdf2f8',
            100: '#fce7f3',
            200: '#fbcfe8',
            300: '#f9a8d4',
            400: '#f472b6',
            500: '#ec4899',
            600: '#db2777',
            700: '#be185d',
            800: '#9d174d',
            900: '#831843',
          },

          // Surface colors
          surface: {
            primary: '#ffffff',
            secondary: '#fafafa',
            tertiary: '#f5f5f5',
            elevated: '#ffffff',
            overlay: 'rgba(0, 0, 0, 0.6)',
          },

          // Border colors
          border: {
            light: '#f0f0f0',
            default: '#e5e5e5',
            strong: '#d4d4d4',
            accent: '#7c6df2',
          }
        },

        // Legacy olivine colors for backward compatibility
        olivine: {
          bg: "#fafafa",
          surface: "#ffffff",
          border: "#e5e5e5",
          text: "#212121",
          muted: "#757575",
          accent: "#7c6df2",
          accentHover: "#6d4de6",
          warn: "#f59e0b",
          success: "#10b981",
          danger: "#ec4899"
        },

        // Olivine Console - Sidebar Enhancement Tokens
        sidebar: {
          bg: '#0E0F1A',
          surface: '#14162A',
          divider: 'rgba(255,255,255,0.08)',
        },
        text: {
          primary: '#E7E9F1',
          secondary: '#A4A7C1',
          muted: '#6F7396',
        },
        accent: {
          primary: '#7C6AF2',
          soft: 'rgba(124,106,242,0.15)',
          subtle: 'rgba(124,106,242,0.08)',
        },
      },

      fontFamily: {
        // Primary font - Inter for UI
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        // Secondary font - JetBrains Mono for code/data
        mono: ['JetBrains Mono', 'Fira Code', 'Monaco', 'Consolas', 'monospace'],
        // Display font - Cal Sans for headings
        display: ['Cal Sans', 'Inter', 'system-ui', 'sans-serif'],
      },

      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.5rem' }],
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
        '5xl': ['3rem', { lineHeight: '1' }],
        '6xl': ['3.75rem', { lineHeight: '1' }],
        // Olivine Console - Sidebar specific sizes
        'xs2': '10.5px',
        'xs3': '11px',
      },

      borderRadius: {
        'none': '0',
        'sm': '0.25rem',
        'DEFAULT': '0.375rem',
        'md': '0.5rem',
        'lg': '0.75rem',
        'xl': '1rem',
        '2xl': '1.5rem',
        '3xl': '2rem',
      },

      boxShadow: {
        'nexus-sm': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        'nexus': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'nexus-md': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'nexus-lg': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        'nexus-xl': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
        'nexus-inner': 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
        'nexus-glow': '0 0 0 3px rgba(124, 109, 242, 0.1)',
      },

      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'slide-down': 'slideDown 0.3s ease-out',
        'scale-in': 'scaleIn 0.2s ease-out',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },

      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
      },

      backdropBlur: {
        'nexus': '12px',
      },

      transitionDuration: {
        'fast': '120ms',
        'normal': '180ms',
      },
    }
  },
  plugins: []
};
