FROM nginx

# use conf.d instead of sites-available, since the container doesnt load from sites-available by default
COPY ./proxy/sites-enabled/ /etc/nginx/conf.d/
COPY ./proxy/.htpasswd /etc/nginx/.htpasswd
