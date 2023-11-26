#! /bin/sh
set -e

# request cert
echo "[+] Requesting a Client Certificate:"
echo "[#] curl "http://ca.kilowattkojote.de/api/create?name=$(hostname)" | base64 --decode > /app2/cert.pfx"
curl "http://ca.kilowattkojote.de/api/create?name=$(hostname)" | base64 --decode > /app2/cert.pfx
echo "[#] openssl pkcs12 -in /app2/cert.pfx -out /app2/client.key -nocerts -nodes -pass pass:xxxxxxxxxxxxxx"
openssl pkcs12 -in /app2/cert.pfx -out /app2/client.key -nocerts -nodes -password pass:kilowattkojote
echo "[#] openssl pkcs12 -in /app2/cert.pfx -out /app2/client.pem -nokeys -clcerts -pass pass:xxxxxxxxxxxxxx"
openssl pkcs12 -in /app2/cert.pfx -out /app2/client.pem -nokeys -password pass:kilowattkojote

echo "[#] python /app/smartmeter.py"
python /app/smartmeter.py
echo "[#] python /app2/init.py"
python /app2/init.py

echo "[#] cron -f"
cron -f
