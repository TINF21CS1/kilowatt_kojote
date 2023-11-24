#! /bin/sh

# request cert
curl "http://ca.kilowattkojote.de/api/create?name=$(hostname)" | base64 --decode > /app2/cert.pfx

cron

python smartmeter.py
