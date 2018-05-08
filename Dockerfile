FROM python:2.7-alpine

COPY . .

RUN pip install behave mock jinja2

RUN python -B -m behave

ENTRYPOINT ['python -B .']
