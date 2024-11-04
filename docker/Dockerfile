#Using officilal container python 3.10 and alpine 3.20
FROM python:3.10-alpine3.20

RUN apk update
RUN apk upgrade
RUN apk add jq
RUN apk add yq-go
RUN pip install pip
RUN pip3 install --user pipenv

# --system to install all packages from Pipfile globally
#RUN python3 -m pipenv install --system
