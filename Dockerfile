FROM python:3.11.6

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/

RUN pip3 install poetry --only main

RUN poetry install

COPY . .
