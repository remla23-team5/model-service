# model-service

## Instructions for running

a) Build the image and run it

`$ docker build . -t ghcr.io/remla23-team5/model-service:0.0.1`

`$ docker run -it --rm -p8080:8080 ghcr.io/remla23-team5/model-service:0.0.1`

## Instructions for connecting to the service

The container should allow you to interact with the Swagger front-end via [localhost:8080/apidocs](http://localhost:8080/apidocs).

