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
