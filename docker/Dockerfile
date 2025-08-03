FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    clang \
    make \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

# ... existing code ... 