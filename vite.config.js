import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: './assets',
  base: '/static/',
  
  build: {
    manifest: true,
    outDir: '../static/vite',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'assets/js/main.js'),
        htmx: resolve(__dirname, 'assets/js/htmx-config.js'),
        alpine: resolve(__dirname, 'assets/js/alpine-config.js'),
      },
    },
  },
  
  server: {
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
    },
    hmr: {
      host: 'localhost',
    },
  },
  
  resolve: {
    alias: {
      '@': resolve(__dirname, 'assets'),
    },
  },
});