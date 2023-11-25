#! /bin/sh
set -e

# request cert
echo "[+] Requesting a Client Certificate:"
echo "[#] curl "http://ca.kilowattkojote.de/api/create?name=$(hostname)" | base64 --decode > /app2/cert.pfx"
curl "http://ca.kilowattkojote.de/api/create?name=$(hostname)" | base64 --decode > /app2/cert.pfx

echo "[#] cron"
cron

echo "[#] python /app2/init.py"
python /app2/init.py
echo "[#] python /app/smartmeter.py"
python /app/smartmeter.py
