FROM python:3.11-alpine

ENV USER=10014

USER 10014

RUN pip3 install -r requirements.txt

COPY . .
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]