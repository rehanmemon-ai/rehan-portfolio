# Privacy, PII Protection & Document Sanitization Policy

Candidate privacy firewall and public document sanitization standards for the portfolio repository.

---

## 1. Absolute PII Prohibitions

The following information must **NEVER** appear in any tracked file, source script, generated HTML page, SVG, image asset, or PDF:

1. **Government Identity Numbers:** Aadhaar (with or without separators), PAN, passport, or voter IDs.
2. **Institutional & Examination Roll Numbers:** University seat numbers, college PRN, or ISRO/IIRS registration/serial codes.
3. **Financial & Contractual Terms:** Monthly stipend figures, salary terms, bank/IFSC/UPI details, or confidential proprietary clauses.
4. **Withheld Document IDs & Local Machine Paths:** Cloud file IDs for intentionally withheld letters, and absolute local OS directory paths under user home directories or private drives.

---

## 2. Confidential Store Separation

Private original records, career archives, and confidential internship folders remain in separate private storage outside the public Git repository and are never indexed or copied into public routes or documentation.

---

## 3. Public-Safe Derivative Pipeline

1. **IIRS / ISRO Outreach (`assets/documents/iirs-outreach/`):** Rendered into 21 public-safe PDFs with registration numbers, QR/barcodes, and verification serials masked.
2. **Internship Reference Offers (`assets/documents/appointment-only-offers/`):** Rendered into 5 sanitized PDFs with candidate PII and compensation terms redacted.
3. **Public Google Drive Assets:** Only explicitly approved read-only (`anyone/reader`) files are linked in `build_site.py`. Confidential offer letters (e.g., Advfiction AI Automation offer) are described as withheld without exposing raw Drive file IDs.

---

## 4. Automated Pre-Commit Privacy Verification

Run `python -B check_site.py` (which checks HTML, source Python/JS files, and `docs/*.md` for local machine paths, withheld Drive IDs, and unsafe URI schemes) and scan with the command below before staging:

```bash
python -c "
import pathlib, re
patterns = [
    re.compile(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'),
    re.compile(r'[A-Za-z]:\\\\(?:Users|_Rehan|Documents)'),
]
for p in pathlib.Path('.').rglob('*'):
    if any(part in {'.git', 'node_modules', '__pycache__', '.venv'} for part in p.parts):
        continue
    if p.is_file() and p.suffix in {'.html', '.js', '.py', '.css', '.md', '.svg'}:
        text = p.read_text(encoding='utf-8', errors='ignore')
        for pat in patterns:
            if pat.search(text):
                print(f'POTENTIAL PRIVACY HIT in {p}: {pat.pattern}')
"
```
