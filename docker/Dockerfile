#Using officilal container python 3.10 and alpine 3.20
FROM python:3.10-alpine3.20

RUN apk update
RUN apk upgrade
# install erquired packages jq and yq
RUN apk add jq
RUN apk add yq-go
RUN pip install pip
RUN apk add bash
RUN apk add git

RUN mkdir /opt/runner
#COPY personas.json /opt/runner/personas.json
#COPY welcome_person.py /opt/runner/welcome_person.py
COPY Pipfile /opt/runner/Pipfile
COPY Pipfile.lock /opt/runner/Pipfile.lock
WORKDIR /opt/runner

RUN pip install --user pipenv
# --system to install all packages from Pipfile globally
RUN python -m pipenv install --system --deploy

#CMD ["python3", "welcome_person.py"]
