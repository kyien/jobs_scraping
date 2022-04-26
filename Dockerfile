FROM python:3.8-slim-buster

RUN mkdir /usr/src/app

ADD . /usr/src/app

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt update --no-cache && \
apt add --no-cache python3-dev gcc libc-dev g++ postgresql-dev cargo libffi-dev musl-dev zlib-dev jpeg-dev && \
pip install --no-cache-dir --upgrade pip setuptools wheel && \
pip install --no-cache-dir -r requirements.txt

CMD ["python","-u", "app.py"]
