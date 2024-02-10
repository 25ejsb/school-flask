FROM python:3-alpine3.10 AS builder
 
WORKDIR /app
 
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
 
# Stage 2
FROM python:3-alpine3.10 AS runner
 
WORKDIR /app
 
COPY --from=builder /app/venv venv
COPY app.py app.py
 
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP=app/app.py
 
EXPOSE 8080
 
CMD ["gunicorn", "--worker-class" , "eventlet", "-w", "1", "app:app"]