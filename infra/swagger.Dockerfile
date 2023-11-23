FROM node AS build

RUN npm install -g redoc-cli
COPY swagger.yaml ./swagger.yaml
RUN redoc-cli bundle -o index.html swagger.yaml

FROM nginx

COPY --from=build index.html /usr/share/nginx/html/index.html
