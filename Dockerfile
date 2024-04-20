FROM python:3-alpine AS builder

ENV USER=10014

USER 10014
 
WORKDIR /flask-app
RUN python3 -m venv env
RUN source ./env/bin/activate 
COPY requirements.txt requirements.txt
RUN sudo pip install -r requirements.txt

COPY . .
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]