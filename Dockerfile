FROM python:3-alpine AS builder

RUN useradd -ms /bin/bash newuser
USER newuser
WORKDIR /home/newuser
 
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]