#Using officilal container python 3.10 and alpine 3.20
FROM python:3.10-alpine3.20

RUN apk update
RUN apk upgrade
# install erquired packages jq and yq
RUN apk add jq
RUN apk add yq-go
RUN pip install pip

RUN mkdir /opt/runner
COPY personas.json /opt/runner/personas.json
COPY welcome_person.py /opt/runner/welcome_person.py
WORKDIR /opt/runner

RUN pip3 install --user pipenv
# --system to install all packages from Pipfile globally
RUN python3 -m pipenv install --system
ENV PYTHONPATH=$PYTHONPATH:/opt/runner/

CMD ["python3", "welcome_person.py"]
