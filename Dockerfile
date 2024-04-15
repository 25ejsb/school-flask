FROM python:3-alpine AS builder

RUN useradd -ms /bin/bash newuser -u 10001
USER newuser
 
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]