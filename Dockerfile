FROM python:3.7-slim-stretch

WORKDIR /app

COPY . /app
ADD . .

EXPOSE 8080

RUN pipenv install

CMD [ "python", "/app/main.py" ]