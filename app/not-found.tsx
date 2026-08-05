export default function NotFound() {
  return (
    <main id="main-content" className="section">
      <div className="container next-offline-card">
        <span className="eyebrow">404</span>
        <h1>Page not found</h1>
        <p>The requested learning page does not exist or its address has changed.</p>
        <div className="next-offline-actions">
          <a className="button primary" href="/">Return home</a>
          <a className="button ghost" href="/tutorials/">Browse tutorials</a>
        </div>
      </div>
    </main>
  );
}
