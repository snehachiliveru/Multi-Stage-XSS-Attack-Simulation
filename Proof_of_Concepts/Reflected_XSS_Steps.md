# Reflected XSS — Steps & Payloads

Vulnerable page: `/dvwa/vulnerabilities/xss_r/` (query parameter `name`)

**Benign payload (example):**
`<script>alert('Reflected XSS - POC-UID-10001')</script>`

**Steps**
1. Login to DVWA.
2. In attacker VM, navigate to:
   `/dvwa/vulnerabilities/xss_r/?name=<script>alert('Reflected XSS - POC-UID-10001')</script>`
3. Observe alert and capture screenshots and URL.
4. Save browser console output (HAR) and server access log lines containing the POC-UID.