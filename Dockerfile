FROM python:3-alpine AS builder

ENV USER=10014

USER 10014
 

WORKDIR /flask-app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]