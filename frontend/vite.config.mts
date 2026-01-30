import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig({
  plugins: [react()],
  resolve: {
    dedupe: ["react", "react-dom", "react-router", "react-router-dom"],
    alias: {
      "@retail": path.resolve(__dirname, "../Retail/frontend"),
      "@hrm": path.resolve(__dirname, "../HRM/frontend"),
      "@fms": path.resolve(__dirname, "../FMS/frontend"),
      "@crm": path.resolve(__dirname, "../CRM/frontend"),
      "@meet": path.resolve(__dirname, "../Meet/frontend"),
      "@core": path.resolve(__dirname, "../core/frontend"),
      "@core/ui-canon": path.resolve(__dirname, "../core/frontend/ui-canon"),
      "@ui": path.resolve(__dirname, "src/components/ui"),
      "@app": path.resolve(__dirname, "src/app"),
      "@services": path.resolve(__dirname, "src/services"),
      "@auth": path.resolve(__dirname, "src/auth"),
      "@contexts": path.resolve(__dirname, "src/core/contexts"),
      "@hooks": path.resolve(__dirname, "src/hooks"),
      "@config": path.resolve(__dirname, "src/config"),
      "lucide-react": path.resolve(__dirname, "node_modules/lucide-react"),
      "@mui/material": path.resolve(__dirname, "node_modules/@mui/material"),
      "@mui/icons-material": path.resolve(__dirname, "node_modules/@mui/icons-material"),
      "axios": path.resolve(__dirname, "node_modules/axios")
    }
  },
  server: {
    fs: {
      allow: [".."]
    },
    port: 3001,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      }
    }
  },
  build: {
    rollupOptions: {
      external: []  // lucide-react should NOT be external - it should be bundled
    }
  },
  optimizeDeps: {
    include: ['lucide-react']  // Ensure lucide-react is pre-bundled
  }
});
