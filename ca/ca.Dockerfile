FROM debian

RUN apt update && apt install webhook -y
RUN apt update && apt install openssl -y

COPY ./hooks.yaml /etc/webhooks/hooks.yaml
COPY ./create-cert.sh /etc/webhooks/
RUN chmod +x /etc/webhooks/create-cert.sh

CMD webhook -hooks=/etc/webhooks/hooks.yaml -port=80 -urlprefix=api -verbose
