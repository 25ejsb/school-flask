FROM python:3-alpine AS builder

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1001 ubuntu
USER ubuntu
 
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]