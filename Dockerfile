FROM python:3.8-alpine

RUN mkdir /app

ADD . /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add python3-dev gcc libc-dev g++ postgresql-dev cargo libffi-dev musl-dev zlib-dev jpeg-dev

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
