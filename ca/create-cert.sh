#!/bin/sh

# usage: ./create-cert.sh <name>
# creates a new client certificate with the given name

tmpkey=$(mktemp)
tmpcsr=$(mktemp)
tmpcrt=$(mktemp)
tmppfx=$(mktemp)

openssl genpkey -algorithm ED25519 -out ${tmpkey}
openssl req -new -nodes -subj "/C=DE/ST=Baden-Württemberg/L=Mannheim/CN=${1}" -out ${tmpcsr} -key ${tmpkey}
openssl x509 -req -days 90 -in ${tmpcsr} -CA ca.crt -CAkey ca.key -out ${tmpcrt} > /dev/null 2>&1
openssl pkcs12 -export -passout pass:kilowattkojote -inkey ${tmpkey} -in ${tmpcrt} -certfile ca.crt -out ${tmppfx}

base64 ${tmppfx}
