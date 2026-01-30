import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@ui': path.resolve(__dirname, '../../Core/frontend/ui-canon/frontend/ui'),
      '@app': path.resolve(__dirname, '../../frontend/src/app'),
      '@hooks': path.resolve(__dirname, '../../frontend/src/hooks'),
      '@auth': path.resolve(__dirname, '../../frontend/src/auth'),
      '@services': path.resolve(__dirname, '../../frontend/src/services'),
      '@config': path.resolve(__dirname, '../../frontend/src/config')
    }
  },
  server: {
    port: 3001,
    host: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  }
})

