FROM mysql:8

ENV MYSQL_ROOT_PASSWORD=pass
ENV MYSQL_DATABASE=demo

RUN mkdir /opt/custom && echo "Hello" > /opt/custom/info.txt

EXPOSE 3306
