FROM python:3.8-slim-buster

ENV USER=10014

USER 10014
 
WORKDIR /flask-app
RUN python3 -m venv env
RUN . ./env/bin/activate 
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --user

COPY . .
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]