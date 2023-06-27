# model-service
The model-service is responsible for serving the trained model which is trained [here](https://github.com/remla23-team5/model-training).

## Instructions for running

a) Build the image using:

`$ docker build . -t ghcr.io/remla23-team5/model-service:1.0.0`

b) Run the built image using:

`$ docker run -it --rm -p8080:8080 ghcr.io/remla23-team5/model-service:1.0.0`

## OpenAPI documentation with Swagger

The container should allow you to interact with the Swagger front-end via [localhost:8080/apidocs](http://localhost:8080/apidocs).

