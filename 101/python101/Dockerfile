FROM python:3.9-slim as build

RUN apt-get update && apt-get upgrade -y

WORKDIR /source

COPY requirements.txt /source/
COPY . /source/app
RUN python3 -m venv /source/venv
RUN /source/venv/bin/pip install --upgrade pip
RUN /source/venv/bin/pip install --no-cache-dir -r /source/requirements.txt

CMD ["/source/venv/bin/python", "/source/app/app.py"]
