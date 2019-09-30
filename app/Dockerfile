# This sets the base image. In this case, a tiny linux image with python installed
FROM python:3.6-alpine

# This specifys the author of the build image
MAINTAINER riedwaan

# Executes commands - can be multiple RUN commands
RUN pip install flask

# Copies files into a directory in our docker image
COPY . /webapp

# Sets the working directory
WORKDIR /webapp

# Exposes a port
EXPOSE 8080

# Specifies the startup command to be executed whenever the container is started
ENTRYPOINT ["python", "helloapp.py"]

