# Stage 1: Builder
FROM python:3.14.4 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2: Runtime
FROM python:3.14.4

WORKDIR /app

COPY --from=builder /install /usr/local

COPY app/ ./app/

EXPOSE 5000

CMD ["python", "app/main.py"]