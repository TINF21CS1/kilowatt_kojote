FROM nginx:debian

COPY ./proxy/sites-enabled/ /etc/nginx/sites-enabled/
COPY ./proxy/.htpasswd /etc/nginx/.htpasswd
