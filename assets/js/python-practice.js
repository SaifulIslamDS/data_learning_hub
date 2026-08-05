(() => {
  'use strict';
  const VERSION = '314.0.2';
  const INDEX_URL = `https://cdn.jsdelivr.net/pyodide/v${VERSION}/full/`;
  const DATASETS = [
    ['/assets/datasets/python_retail_sales.csv', 'python_retail_sales.csv'],
    ['/assets/datasets/python_customers.csv', 'python_customers.csv'],
    ['/assets/datasets/python_messy_orders.csv', 'python_messy_orders.csv'],
  ];
  let runtimePromise = null;
  let filesReady = false;
  const loadedPackages = new Set();
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

  function loadRuntimeScript() {
    if (window.loadPyodide) return Promise.resolve();
    return new Promise((resolve, reject) => {
      const existing = document.querySelector('script[data-pyodide-runtime]');
      if (existing) {
        existing.addEventListener('load', resolve, {once:true});
        existing.addEventListener('error', () => reject(new Error('Pyodide runtime failed to load.')), {once:true});
        return;
      }
      const script = document.createElement('script');
      script.src = `${INDEX_URL}pyodide.js`;
      script.async = true;
      script.dataset.pyodideRuntime = VERSION;
      script.onload = resolve;
      script.onerror = () => reject(new Error('Pyodide runtime failed to load. Check the internet connection or Content Security Policy.'));
      document.head.appendChild(script);
    });
  }

  async function ensureFiles(pyodide) {
    if (filesReady) return;
    for (const [url, name] of DATASETS) {
      const response = await fetch(url);
      if (!response.ok) throw new Error(`Could not load ${name}.`);
      const bytes = new Uint8Array(await response.arrayBuffer());
      pyodide.FS.writeFile(name, bytes);
    }
    filesReady = true;
  }

  async function runtime(packages = []) {
    if (!runtimePromise) {
      runtimePromise = (async () => {
        await loadRuntimeScript();
        const pyodide = await window.loadPyodide({indexURL: INDEX_URL});
        await ensureFiles(pyodide);
        return pyodide;
      })();
    }
    const pyodide = await runtimePromise;
    const needed = [...new Set(packages)].filter(Boolean).filter(name => !loadedPackages.has(name));
    if (needed.length) {
      await pyodide.loadPackage(needed);
      needed.forEach(name => loadedPackages.add(name));
    }
    return pyodide;
  }

  async function execute(code, packages) {
    const pyodide = await runtime(packages);
    pyodide.globals.set('DLH_USER_CODE', code);
    const result = await pyodide.runPythonAsync(`
import contextlib, io, json, traceback
_DLH_BUFFER = io.StringIO()
_DLH_PLOTS = []
_DLH_OK = True
try:
    with contextlib.redirect_stdout(_DLH_BUFFER), contextlib.redirect_stderr(_DLH_BUFFER):
        exec(DLH_USER_CODE, globals())
    try:
        import matplotlib.pyplot as _dlh_plt
        import base64 as _dlh_base64
        for _dlh_number in _dlh_plt.get_fignums():
            _dlh_fig = _dlh_plt.figure(_dlh_number)
            _dlh_image = io.BytesIO()
            _dlh_fig.savefig(_dlh_image, format='png', dpi=130, bbox_inches='tight')
            _DLH_PLOTS.append(_dlh_base64.b64encode(_dlh_image.getvalue()).decode('ascii'))
        _dlh_plt.close('all')
    except Exception:
        pass
except Exception:
    _DLH_OK = False
    traceback.print_exc(file=_DLH_BUFFER)
json.dumps({'ok': _DLH_OK, 'stdout': _DLH_BUFFER.getvalue(), 'plots': _DLH_PLOTS})
`);
    return JSON.parse(result);
  }

  function markup(code, packages = []) {
    return `<div class="python-practice" data-python-packages="${esc(packages.join(','))}">
      <div class="python-editor-head"><div><strong>Python browser practice</strong><small>Pyodide ${VERSION} · runs locally in this browser</small></div><span class="python-status" data-python-status>Runtime not loaded</span></div>
      <textarea class="python-editor" data-python-editor spellcheck="false" aria-label="Python code editor">${esc(code)}</textarea>
      <div class="python-actions"><button class="button primary small" type="button" data-run-python>Run Python</button><button class="button ghost small" type="button" data-reset-python>Reset</button><button class="button ghost small" type="button" data-copy-python>Copy</button></div>
      <div class="python-output" aria-live="polite"><div class="python-output-head"><strong>Output</strong><span>stdout, errors, and charts</span></div><pre data-python-output>Run the code to see output.</pre><div class="python-plots" data-python-plots></div></div>
      <p class="python-runtime-note">The first run downloads the Python WebAssembly runtime and requested packages. Practice data stays in browser memory and no code is sent to a backend.</p>
    </div>`;
  }

  function bind(root, code, packages = []) {
    const editor = root.querySelector('[data-python-editor]');
    const output = root.querySelector('[data-python-output]');
    const plots = root.querySelector('[data-python-plots]');
    const status = root.querySelector('[data-python-status]');
    const run = root.querySelector('[data-run-python]');
    const initial = code;
    run?.addEventListener('click', async () => {
      run.disabled = true;
      status.textContent = 'Loading Python…';
      output.textContent = 'Preparing runtime and packages…';
      plots.innerHTML = '';
      try {
        const result = await execute(editor.value, packages);
        status.textContent = result.ok ? 'Run complete' : 'Python error';
        output.textContent = result.stdout || (result.ok ? 'Code completed without printed output.' : 'The code failed without an error message.');
        plots.innerHTML = result.plots.map((src, i) => `<figure><img src="data:image/png;base64,${src}" alt="Python chart output ${i+1}"></figure>`).join('');
      } catch (error) {
        status.textContent = 'Runtime error';
        output.textContent = error?.message || String(error);
      } finally {
        run.disabled = false;
      }
    });
    root.querySelector('[data-reset-python]')?.addEventListener('click', () => {
      editor.value = initial; output.textContent = 'Run the code to see output.'; plots.innerHTML = ''; status.textContent = 'Runtime ready to load';
    });
    root.querySelector('[data-copy-python]')?.addEventListener('click', async event => {
      await navigator.clipboard?.writeText(editor.value);
      const button = event.currentTarget; const old = button.textContent; button.textContent = 'Copied'; setTimeout(() => button.textContent = old, 1000);
    });
  }

  function renderActivity(root, activity) {
    const packages = activity.packages || [];
    root.innerHTML = markup(activity.code || "print('Hello, analytics!')", packages);
    bind(root, activity.code || '', packages);
  }

  function renderStandalone(root) {
    const code = `import pandas as pd\n\nsales = pd.read_csv('python_retail_sales.csv', parse_dates=['order_date'])\nsummary = (sales.groupby('region', as_index=False)\n           .agg(orders=('order_id','nunique'),\n                revenue=('revenue','sum'),\n                profit=('profit','sum')))\nprint(summary)`;
    root.innerHTML = markup(code, ['pandas','numpy','matplotlib','scipy']);
    bind(root, code, ['pandas','numpy','matplotlib','scipy']);
  }

  window.DLHPythonPractice = {renderActivity, renderStandalone, execute, version: VERSION};
  document.addEventListener('DOMContentLoaded', () => {
    const root = document.getElementById('python-playground-root');
    if (root) renderStandalone(root);
  });
})();
