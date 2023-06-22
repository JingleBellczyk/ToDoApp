FROM ubuntu 

RUN apt-get update && apt-get -y install \
    python3 \
    python3-pip \
    && pip install pipenv

ENV WORKDIR="/"

COPY . .

EXPOSE 8000