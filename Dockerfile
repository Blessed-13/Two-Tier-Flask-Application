# Dockerfile for Python 3.9 Slim
FROM python:3.9-slim
# Set the working directory
WORKDIR /app
# Install system dependencies -sql
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*
# Copy the requirements file
COPY app/requirements.txt .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application code only
COPY app/ .
# Start the application
CMD [ "gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app" ]