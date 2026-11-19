# Privacy, PII Protection & Document Sanitization Policy

This document codifies the candidate privacy firewall and document protection protocols for the public portfolio repository.

---

## 1. Absolute PII Prohibitions

The following personally identifiable information (PII) must **NEVER** appear in any public file, source code, commit history, HTML page, image asset, or PDF in this repository:

1. **Government Identity Numbers:**
   - Aadhaar numbers (12-digit UIDAI).
   - PAN (Permanent Account Numbers).
   - Passport or voter identification numbers.
2. **Institutional & Examination Roll Numbers:**
   - University examination seat numbers.
   - College PRN (Permanent Registration Numbers).
   - ISRO / IIRS registration numbers or participant serial codes.
3. **Financial Terms & Offer Details:**
   - Monthly stipend amounts, confidential salary numbers, or proprietary client contract terms.
   - Bank details, IFSC codes, or UPI addresses.
4. **Physical Private Addresses:**
   - Specific residential street addresses or house numbers (general city "Mumbai, India" is allowed).

---

## 2. Directory Isolation Rules

Coding agents, automated scripts, and maintainers must strictly respect the privacy firewall:

### Restricted Local Directories (Confidential Document Stores)
- `D:\_Rehan_Career_Audit_Workspace`
- `D:\_Rehan_Antigravity-output\Resume_Portfolio`
- `D:\_Rehan_Antigravity-output\Awarewolf`
- `D:\_Rehan\AwareWolf Internship`
- `D:\_Rehan\Certificate's` (Original certificate archive — strictly READ-ONLY)

These directories contain unredacted legal, academic, and identification documents. They must never be indexed, copied into the public repository, or committed to Git.

---

## 3. Public-Safe Derivative Pipeline

For educational and outreach certificates (e.g. IIRS / ISRO Outreach):
1. **Source Document:** Stored securely in `D:\_Rehan\Certificate's\` or Google Drive Private Vault.
2. **Derivative Creation:** The document is rendered into a public-safe derivative (`rehan-portfolio/assets/documents/iirs-outreach/`) with registration numbers, barcode payloads, and verification serial codes stripped.
3. **Public Exposure:** Only the public-safe derivative is committed to the repository or linked in `build_site.py`.
4. **Cloud Backup:** The derivative is also backed up to `Rehan Portfolio Vault/01_PUBLIC_CERTIFICATES/IIRS_ISRO_Public_Safe_Copies/` with file-level viewer access (`anyone/reader`).

---

## 4. Pre-Commit Privacy Audit Command

Run a regex-based PII audit prior to staging any file:
```bash
# Check for 12-digit numeric strings (potential Aadhaar)
python -c "
import os, re
pattern = re.compile(r'\b\d{4}\s?\d{4}\s?\d{4}\b')
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'docs' in root: continue
    for f in files:
        if f.endswith(('.html', '.js', '.py', '.css', '.md')):
            path = os.path.join(root, f)
            text = open(path, encoding='utf-8', errors='ignore').read()
            if pattern.search(text):
                print(f'POTENTIAL PII DETECTED in {path}')
"
```
