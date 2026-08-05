import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";
import "./next-overrides.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://datalearninghub.netlify.app"),
  title: { default: "Data Learning Hub", template: "%s | Data Learning Hub" },
  description: "A bilingual Data Analytics learning platform covering foundations, statistics, Excel, SQL, Power BI, Python, workflows, and portfolio projects.",
  applicationName: "Data Learning Hub",
  manifest: "/manifest.webmanifest",
  alternates: { canonical: "/" },
  icons: {
    icon: [{ url: "/assets/icons/favicon.svg", type: "image/svg+xml" }, { url: "/icons/icon-192.png", sizes: "192x192", type: "image/png" }],
    apple: [{ url: "/icons/apple-touch-icon.png", sizes: "180x180", type: "image/png" }],
  },
  openGraph: {
    type: "website",
    siteName: "Data Learning Hub",
    url: "https://datalearninghub.netlify.app",
    images: ["/assets/icons/social-card.svg"],
  },
  twitter: { card: "summary_large_image", images: ["/assets/icons/social-card.svg"] },
};

export const viewport: Viewport = {
  themeColor: [{ media: "(prefers-color-scheme: light)", color: "#6257e8" }, { media: "(prefers-color-scheme: dark)", color: "#15132a" }],
  width: "device-width",
  initialScale: 1,
};

function FallbackHeader() {
  return (
    <header className="site-header" id="site-header-bar">
      <div className="container navbar">
        <a className="brand" href="/" aria-label="Data Learning Hub home">
          <span className="brand-mark" aria-hidden="true">
            <svg viewBox="0 0 24 24"><path d="M5 18V8m5 10V4m5 14v-7m4 7V6" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/><path d="M3 20h18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/></svg>
          </span>
          <span className="brand-text">Data Learning Hub<small>Analytics first · careers next</small></span>
        </a>
        <nav className="nav-links" aria-label="Primary navigation">
          <a href="/tutorials/">Tutorials</a>
          <a href="/exercises/">Exercises</a>
          <a href="/examples/">Examples</a>
          <a href="/projects/">Projects</a>
          <a href="/references/">References</a>
          <a href="/career-paths/">Career Paths</a>
        </nav>
      </div>
    </header>
  );
}

function FallbackFooter() {
  return (
    <footer className="site-footer">
      <div className="container footer-bottom">
        <span>Idea and developed by Saiful Islam.</span>
        <div className="footer-bottom-links"><a href="/about/">About</a></div>
      </div>
    </footer>
  );
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" data-theme="light" suppressHydrationWarning>
      <head>
        <link rel="stylesheet" href="/assets/css/main.css" />
        <script src="/assets/js/theme-init.js" />
      </head>
      <body suppressHydrationWarning>
        <a className="skip-link" href="#main-content">Skip to content</a>
        <div id="site-header"><FallbackHeader /></div>
        {children}
        <div id="site-footer"><FallbackFooter /></div>
        <div id="search-root" />
        <button className="scroll-top" id="scroll-top" type="button" aria-label="Scroll to top" title="Scroll to top">↑</button>
        <script dangerouslySetInnerHTML={{ __html: `
          if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
              navigator.serviceWorker.register('/sw.js').catch((error) => console.warn('[DLH PWA]', error));
            });
          }
        ` }} />
      </body>
    </html>
  );
}
