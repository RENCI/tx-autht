FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev make
RUN pip3 install --no-cache-dir flask flask-cors greenlet==0.4.16 gevent==1.4.0 gunicorn==19.9.0 connexion[swagger-ui] requests tx-functional python-dateutil

COPY api /usr/src/app/api
COPY tx-utils/src /usr/src/app

EXPOSE 8080

ENTRYPOINT ["gunicorn"]

CMD ["-w", "4", "-b", "0.0.0.0:8080", "--worker-class", "gevent", "api.server:create_app()"]
