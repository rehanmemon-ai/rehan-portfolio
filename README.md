# Rehan Memon portfolio

A dependency-free static portfolio. The fourteen HTML pages are generated from reviewed content in `build_site.py`; `site.css`, `site.js`, and `favicon.svg` are local assets. The Phase 1 `style.css` and `main.js` files are retained for worktree preservation but are no longer loaded by generated pages.

## Edit and preview

Edit the content and templates in `build_site.py`, then run:

```powershell
python build_site.py
python -B check_site.py
node --check site.js
python -m http.server 8000
```

Open `http://localhost:8000/`. To emulate GitHub Pages under `/rehan-portfolio/`, serve a parent folder containing this repository as a `rehan-portfolio` directory, or use the local preview helper documented in the private Phase 2 test report. All page links and assets are relative to the current HTML file, and all generated pages live in the repository root.

No dependency installation, backend, form provider, analytics or tracking is required.

## Publication review

The internal evidence register and asset manifest are held outside this public repository. Before a release, verify every new claim against original evidence, confirm rights for each visual or certificate, decide the canonical host, run both hosting-path tests, and check external destinations. There is no public resume download or certificate PDF preview until a redacted, approved asset exists.
