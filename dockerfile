FROM python:3.8-slim-buster


COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv lock -r > requirements.txt


RUN pip install -r requirements.txt


EXPOSE 8000

COPY ./forests_api ./forests_api

CMD exec uvicorn forests_api.main:app --host 0.0.0.0