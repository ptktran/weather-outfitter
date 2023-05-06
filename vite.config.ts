import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
  server: {
    port: 1234,
    strictPort: false,
  },
  preview: {
    port: 5678,
    strictPort: false,
  }
});
