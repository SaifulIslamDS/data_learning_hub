import type { LegacyPageData } from "@/src/lib/page-data";

function serialize(value: unknown): string {
  return JSON.stringify(value).replace(/</g, "\u003c");
}


function prepareTutorialHtml(html: string): string {
  return html
    .replace(/<a href="#objectives">Objectives<\/a>/g, "")
    .replace(/<section class="tutorial-section tutorial-objectives" id="objectives">[\s\S]*?<\/section>/g, "")
    .replace('<span class="stat-chip"><strong>EN/BN</strong> bilingual</span>', '<span class="stat-chip"><strong>Practice</strong> built in</span>')
    .replace('<span><strong>EN/BN</strong> bilingual</span>', '<span><strong>English</strong> tutorial</span>');
}

export function LegacyPage({ page }: { page: LegacyPageData }) {
  const renderedHtml = prepareTutorialHtml(page.mainHtml);
  const boot = `
    (() => {
      const bodyAttrs = ${serialize(page.bodyAttrs)};
      for (const [key, value] of Object.entries(bodyAttrs)) {
        const attr = key.startsWith('data-') ? key : key;
        document.body.setAttribute(attr, Array.isArray(value) ? value.join(' ') : String(value));
      }

      const loadScript = (src) => new Promise((resolve, reject) => {
        const existing = document.querySelector('script[data-dlh-runtime="' + CSS.escape(src) + '"]');
        if (existing) { resolve(); return; }
        const script = document.createElement('script');
        script.src = src;
        script.async = false;
        script.dataset.dlhRuntime = src;
        script.onload = () => resolve();
        script.onerror = () => reject(new Error('Failed to load ' + src));
        document.body.appendChild(script);
      });

      const start = async () => {
        try {
          await loadScript('/assets/js/content.js');
          await loadScript('/assets/js/site.js');
          const scripts = ${serialize(page.scripts)};
          for (const src of scripts) await loadScript(src);
          const inlineScripts = ${serialize(page.inlineScripts)};
          for (const source of inlineScripts) {
            const script = document.createElement('script');
            script.textContent = source;
            document.body.appendChild(script);
          }
          window.dispatchEvent(new CustomEvent('dlh:next-page-ready', { detail: ${serialize(page.route)} }));
        } catch (error) {
          console.error('[DLH runtime]', error);
        }
      };
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', start, { once: true });
      } else {
        start();
      }
    })();
  `;

  return (
    <>
      <div className="next-page-host" dangerouslySetInnerHTML={{ __html: renderedHtml }} />
      <script dangerouslySetInnerHTML={{ __html: boot }} />
    </>
  );
}
