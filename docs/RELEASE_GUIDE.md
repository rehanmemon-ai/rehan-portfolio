# Release & Quality Assurance Guide

This runbook defines the mandatory verification, branch governance, and release protocol for the portfolio repository.

---

## 1. Release Governance & Branch Policies

### Strict Prohibitions
- **NEVER** run `git push origin main` directly.
- **NEVER** run `git commit -a` without staged review.
- **NEVER** run `git reset --hard` or `git clean -fd`.
- **NEVER** trigger automatic production deployments without explicit sign-off.

### Standard Release Workflow
1. Create a feature branch: `git checkout -b feat/<release-name>`
2. Execute edits in `build_site.py`, `site.css`, `site.js`, or documentation.
3. Rebuild the static HTML files: `python build_site.py`
4. Run the automated audit suite: `python check_site.py`
5. Verify JavaScript syntax: `node --check site.js`
6. Review changes: `git diff`
7. Stage files deliberately: `git add <file1> <file2> ...`
8. Commit with a descriptive message: `git commit -m "feat: description"`
9. Create a remote backup branch if performing major structural updates.

---

## 2. Automated Pre-Flight Checklist

Before proposing or merging any release candidate, run the full verification gate:

```bash
# 1. Recompile all routes
python build_site.py

# 2. Automated Quality Audit
python check_site.py
```

### What `check_site.py` Validates
- **Route Completeness:** Checks that all 17 declared `.html` routes exist and are non-empty.
- **Heading Hierarchy:** Enforces that every page has exactly one `<h1>`.
- **Internal Anchor Integrity:** Parses all `<a href="#id">` and `<a href="page.html#id">` to ensure every target anchor ID exists in the destination document.
- **Asset Resolution:** Confirms that every local `<img>`, `<link rel="icon">`, and local `<a href="assets/...">` file exists on disk.
- **Outbound Link Hygiene:** Checks for broken protocols or malformed URLs.

---

## 3. Manual Browser Inspection Protocol

Before approving a release for external recruiters, verify visual appearance on desktop and mobile viewports:

1. Launch a local web server:
   ```bash
   python -m http.server 8765
   ```
2. Open `http://127.0.0.1:8765/` in your browser.
3. Verify the following critical routes:
   - **Homepage (`index.html`):** Hero headline, navigation links, quick bio, flagship project cards.
   - **Credentials (`credentials.html`):** Search bar and filter tabs function smoothly; card action buttons are pinned neatly to the bottom.
   - **ConnectHub (`connecthub.html`):** Live demo link (`https://connecthub-web-w89e.onrender.com`), architecture diagram, and test accounting.
   - **Activities (`activities.html`):** Public Speaking & Event Hosting is in Position 2; DLLE 120+ hours card displays properly.
   - **Contact (`contact.html`):** Email copy action copies `memon18rehan@gmail.com` to the clipboard.
