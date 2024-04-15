FROM python:3-alpine AS builder

ENV USER=10014

RUN useradd -rm -d /home/10014 -s /bin/bash -g root -G sudo -u 10014
USER ubuntu
 
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]