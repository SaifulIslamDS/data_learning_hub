export const metadata = { title: "Offline", description: "Offline fallback for Data Learning Hub." };

export default function OfflinePage() {
  return (
    <main id="main-content" className="section">
      <div className="container next-offline-card">
        <span className="eyebrow">Offline mode</span>
        <h1>You are currently offline.</h1>
        <p>Previously visited tutorials and local assets may still be available. SQL and Python browser runtimes can require an online first load.</p>
        <div className="next-offline-actions">
          <a className="button primary" href="/">Reconnect and return home</a>
          <a className="button ghost" href="/tutorials/">Open cached tutorials</a>
        </div>
      </div>
    </main>
  );
}
