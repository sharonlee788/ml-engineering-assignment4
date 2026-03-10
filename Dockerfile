FROM python:3.11-slim

WORKDIR /app

COPY app.py /app/

RUN mkdir -p /app/data

CMD ["python", "app.py"]