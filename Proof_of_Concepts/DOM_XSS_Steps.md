# DOM-based XSS — Steps & Payloads

Vulnerable page: DVWA page that echoes `location.hash` or `location.search` unsafely.

**Benign payload (example, append after #):**
`#<img onerror="alert('DOM XSS POC - POC-UID-30003')">`

**Steps**
1. Navigate to the vulnerable page and append the above hash to URL.
2. Reload, observe alert or DOM change.
3. Capture DevTools screenshot showing where `location.hash` was used.