# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

WORKDIR /app
COPY requirements.txt /app/
# COPY . /app
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
RUN apt-get update
# ENV SECRET_KEY='JGDg8NHvsKf6vydp3aJtMw=='
#    apt-get install net-tools \
#    apt-get install iputils-ping
CMD [ "python3", "-m" , "flask", "run", "-p", "5000", "--host=0.0.0.0" ]
# MUST INCLUDE "--host=0.0.0.0" in CMD regardless of if running individual docker container locally,
## with docker compose or as pod hosted on kubelet worker node. Setting host to 0.0.0.0 allows outside
### connections, else localhost will only apply to the container's local host.
# CMD [ "python3", "-m", "flask", "run" ]
# CMD [ "python3", "run.py" ]
# CMD [ "python3"]