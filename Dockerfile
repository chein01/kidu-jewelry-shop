FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=Asia/Ho_Chi_Minh

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    vim-tiny \
    python3-pip \
    default-libmysqlclient-dev \
    git \
    gcc \
    wget \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/code
WORKDIR /app/code

COPY requirements.txt /app/code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/code/

COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8000

