FROM swaggerapi/swagger-ui

COPY swagger.yaml /app/swagger.yaml
ENV SWAGGER_JSON="/app/swagger.yaml"
ENV PORT="8080" \
    PORT_IPV6="8080"
