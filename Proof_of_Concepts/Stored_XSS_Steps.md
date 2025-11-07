# Stored XSS — Steps & Payloads

Vulnerable page: `/dvwa/vulnerabilities/xss_s/` (message board)

**Benign payload (example):**
`<script>document.body.insertAdjacentHTML('afterbegin','<div id="poc">Stored XSS POC - POC-UID-20002</div>')</script>`

**Steps**
1. While logged in, post the above payload as a comment.
2. Visit the page rendering stored comments; observe inserted DOM element.
3. Capture screenshots, server logs, and browser HAR.