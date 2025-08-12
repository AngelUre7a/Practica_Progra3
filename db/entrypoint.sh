#!/bin/sh
DB_FILE="/data/mydb.sqlite"

# Crear DB si no existe
if [ ! -f "$DB_FILE" ]; then
    echo "Creando base de datos inicial..."
    sqlite3 "$DB_FILE" < /init.sql
else
    echo "Base de datos ya existente, no se recrea."
fi

exec "$@"
