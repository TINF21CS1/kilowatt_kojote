FROM debian

RUN apt update && apt install webhook -y
RUN apt update && apt install openssl -y

COPY ./hooks.yaml /etc/webhooks/hooks.yaml
COPY ./*.sh /etc/webhooks/

CMD ["webhook", "-hooks=/etc/webhooks/hooks.yaml"]
