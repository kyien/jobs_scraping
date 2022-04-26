FROM python:3.8-alpine

RUN mkdir /usr/src/app

ADD . /usr/src/app

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /usr/local/lib/python3.8/site-packages

RUN apk update  && \
apk add --no-cache python3-dev gcc libc-dev g++ postgresql-dev cargo libffi-dev musl-dev zlib-dev jpeg-dev && \
pip install --no-cache-dir --upgrade pip setuptools wheel && \
pip install --no-cache-dir requests && \
pip install --no-cache-dir -r requirements.txt

CMD ["python","-u", "app.py"]
