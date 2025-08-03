FROM python:3.11

WORKDIR /workspace

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y git curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt 