#! /bin/bash
set -e

if [[ "$(cat /app/init_complete)" == "1" ]]; then
    echo "[+] init already completed, starting running config"

    echo "[#] python /app/smartmeter.py"
    python /app/smartmeter.py > /proc/1/fd/1 2>/proc/1/fd/2 &
else
    # request cert
    echo "[+] Requesting a Client Certificate:"
    echo "[#] curl "http://ca.kilowattkojote.de/api/create?name=$(hostname)" | base64 --decode > /app/cert.pfx"
    curl "http://ca.kilowattkojote.de/api/create?name=$(hostname)" | base64 --decode > /app/cert.pfx
    echo "[#] openssl pkcs12 -in /app/cert.pfx -out /app/client.key -nocerts -nodes -pass pass:xxxxxxxxxxxxxx"
    openssl pkcs12 -in /app/cert.pfx -out /app/client.key -nocerts -nodes -password pass:kilowattkojote
    echo "[#] openssl pkcs12 -in /app/cert.pfx -out /app/client.pem -nokeys -clcerts -pass pass:xxxxxxxxxxxxxx"
    openssl pkcs12 -in /app/cert.pfx -out /app/client.pem -nokeys -password pass:kilowattkojote

    echo "[#] python /app/smartmeter.py"
    python /app/smartmeter.py > /proc/1/fd/1 2>/proc/1/fd/2 &
    echo "[#] python /app/meter_software_init.py"
    python /app/meter_software_init.py

    echo "[+] adding random offset to cronjob"
    # random offset
    rand=$(python -c "import random; print(random.randint(0,14))")
    rand1=${rand}
    rand2=$((rand+15))
    rand3=$((rand+30))
    rand4=$((rand+45))
    sed -i "s/0,15,30,45/${rand},${rand2},${rand3},${rand4}/g" /etc/cron.d/meter.cron
    crontab /etc/cron.d/meter.cron
    echo "[+] added random offset '${rand}' and installed new crontab"

    echo "1" > /app/init_complete
fi

echo "[#] cron -f"
cron -f
