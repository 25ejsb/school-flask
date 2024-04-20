FROM ubuntu:latest

ENV USER=10014

USER 10014

RUN sudo apt update
RUN sudo apt install python3 python3-pip gunicorn -y
 
WORKDIR /flask-app
RUN python3 -m venv env
RUN source ./env/bin/activate 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]