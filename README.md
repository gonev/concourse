# Resources
Concourse UI: http://ec2-52-58-155-219.eu-central-1.compute.amazonaws.com:8080

DockerHub: https://hub.docker.com/u/ggonev

# Bringup Concourse

>wget https://concourse-ci.org/docker-compose.yml

>docker-compose up -d

# Build Docker image
>docker build --no-cache -t ggonev/hello-sap-python3.10-alpine3.20 .

>docker push ggonev/hello-sap-python3.10-alpine3.20

# Concourse piplines
>fly -t main sp -p hello-sap -c hello_sap.yml

>fly -t main sp -p hello-sap -c pipelines/pipeline_hello_sap.yml

