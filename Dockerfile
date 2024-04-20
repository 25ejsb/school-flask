FROM python:3-alpine AS builder

ENV USER=10014

RUN source ./school-flask/bin/activate

USER 10014
 
WORKDIR .
COPY . .
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]