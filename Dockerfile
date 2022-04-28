
# Stage 1 - Install build dependencies
FROM python:3.8-alpine AS base
RUN mkdir /svc
WORKDIR /svc
# RUN python -m venv .venv && .venv/bin/pip install --no-cache-dir -U pip setuptools wheel
COPY requirements.txt .

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*
    

RUN apk update  && \
 apk add --no-cache python3-dev gcc libc-dev libstdc++ g++ postgresql-dev cargo libffi-dev musl-dev zlib-dev jpeg-dev && \
 rm -rf /var/cache/apk/*  && \
 pip wheel -r requirements.txt --wheel-dir=/svc/wheels

# Stage 2 - Copy only necessary files to the runner stage
FROM python:3.8-alpine

# RUN apk add --no-cache \
#     jpeg-dev zlib-dev \
#     libmagic

COPY --from=base /svc /svc

WORKDIR /svc
RUN pip install --no-index --no-build-isolation --find-links=/svc/wheels -r requirements.txt 

RUN mkdir /usr/src/app

WORKDIR /usr/src/app
COPY . ./

#ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "app.py"]


# FROM python:3.8-slim-stretch

# RUN mkdir /usr/src/app

# ADD . /usr/src/app

# WORKDIR /usr/src/app

# ENV PYTHONDONTWRITEBYTECODE 1

# ENV PYTHONUNBUFFERED 1

# ENV PYTHONPATH /usr/local/lib/python3.8/site-packages

# RUN apt-get update  && \
# apt-get  --no-cache python3-dev gcc libc-dev g++ postgresql-dev cargo libffi-dev musl-dev zlib-dev jpeg-dev && \
# pip install --no-cache-dir --upgrade pip setuptools wheel && \
# pip install --no-cache-dir -r requirements.txt

# CMD ["python","-u", "app.py"]
