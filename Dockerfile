FROM python:3-alpine AS builder

ENV USER=10014

USER 10014
 
WORKDIR .
COPY . .
RUN pip install -r requirements.txt --user
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]