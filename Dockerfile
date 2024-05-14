FROM python:3.8-slim-buster

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip3 install --user -r requirements.txt

COPY . .
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]