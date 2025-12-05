import { createTyEditor } from 'https://shark.fish/ty-embed/ty-embed.es.js';

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.ty-editor').forEach((container) => {
    const template = container.querySelector('script[type="text/template"]');
    const code = template ? template.textContent.trim() : '';
    const height = container.dataset.height || '350px';

    if (template) {
      template.remove();
    }

    createTyEditor({
      container,
      height,
      initialCode: code,
    });
  });
});
