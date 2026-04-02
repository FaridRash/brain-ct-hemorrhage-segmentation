FROM python:3.10-slim

WORKDIR /app

# install minimal system deps
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# Cloud Run uses port 8080
ENV PORT=8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]