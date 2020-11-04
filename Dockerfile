FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y --fix-missing \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential

RUN groupadd -r celery && useradd --no-log-init -r -g celery celery

COPY requirements.txt /code/
RUN python -m pip install --upgrade pip

# clear pip cache
RUN pip install -r requirements.txt --no-cache-dir

COPY . /code/