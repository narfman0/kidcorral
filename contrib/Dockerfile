FROM python:3.7.2-alpine3.9

EXPOSE 8000

WORKDIR /usr/src/app

RUN pip install --no-cache-dir pipenv

COPY . .

RUN apk --no-cache add build-base mariadb-dev

RUN make init && make migrate

CMD [ "make", "rp" ]
