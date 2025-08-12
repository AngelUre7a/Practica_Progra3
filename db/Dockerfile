FROM alpine:3.18

RUN apk add --no-cache sqlite

WORKDIR /data

COPY init.sql /init.sql

# Script de arranque
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["tail", "-f", "/dev/null"]

#jdbc:sqlite:C:/Users/Saul/Documents/Github/Practica_Progra3/db/data/mydb.sqlite