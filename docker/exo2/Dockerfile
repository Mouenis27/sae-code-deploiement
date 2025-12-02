FROM mysql:8

ENV MYSQL_ROOT_PASSWORD=pass
ENV MYSQL_DATABASE=demo

COPY init.sql /docker-entrypoint-initdb.d/
