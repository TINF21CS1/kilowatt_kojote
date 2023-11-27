#! /bin/sh
set -e

# request cert
echo "[+] Requesting a Client Certificate:"
echo "[#] curl "http://ca.kilowattkojote.de/api/create?name=$(hostname)" | base64 --decode > /app/cert.pfx"
curl "http://ca.kilowattkojote.de/api/create?name=$(hostname)" | base64 --decode > /app/cert.pfx
echo "[#] openssl pkcs12 -in /app/cert.pfx -out /app/client.key -nocerts -nodes -pass pass:xxxxxxxxxxxxxx"
openssl pkcs12 -in /app/cert.pfx -out /app/client.key -nocerts -nodes -password pass:kilowattkojote
echo "[#] openssl pkcs12 -in /app/cert.pfx -out /app/client.pem -nokeys -clcerts -pass pass:xxxxxxxxxxxxxx"
openssl pkcs12 -in /app/cert.pfx -out /app/client.pem -nokeys -password pass:kilowattkojote

echo "[#] python /app/smartmeter.py"
python /app/smartmeter.py
echo "[#] python /app/meter_software_init.py"
python /app/meter_software_init.py

echo "[#] cron -f"
cron -f
