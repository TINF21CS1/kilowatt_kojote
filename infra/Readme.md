# Infrastructure Setup

Ansible is meant for the Basis of the Infrastructure. Due to singel use and non-redeployment of this project, not everything is done inside of ansible. Manual steps are documented below.

## Ansible (on the Development Machine)

```
sudo apt install ansible
cd infra
ansible-playbook -i inventory.yml playbook.yml
```

## Infrastructure Setup

The Main System is a Hetzner CAX11 at srv1.kilowattkojote.de

The DNS is also handled by Hetzner and managed manually.

### Getting certificates

```
apt install certbot
certbot certonly --preferred-challenges dns --manual -d kilowattkojote.de -d *.kilowattkojote.de --agree-tos -m s212689@student.dhbw-mannheim.de
```

The matching text record then needs to be added to the DNS. Certs are stored in `/etc/letsencrypt/live/kilowattkojote.de/`

### Basic Auth for Frontend

on the dev machine:

```
apt install apache2-utils
htpasswd infra/files/srv/proxy/.htpasswd <username>
```

### Creating a CA

```
apt install openssl
openssl genpkey -algorithm ED25519 -out ca.key
openssl req -new -x509 -days 90 -key ca.key -out ca.crt
```

```
Country Name (2 letter code) [AU]:DE
State or Province Name (full name) [Some-State]:Baden-Württemberg
Locality Name (eg, city) []:Mannheim
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Kilowattkojote
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:ca.kilowattkojote.de
Email Address []:s212689@student.dhbw-mannheim.de
```
