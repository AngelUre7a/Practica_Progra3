import sqlite3

DB_PATH = 'db/clientes_compras.db'
SCHEMA_PATH = 'schema.sql'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.close()

if __name__ == '__main__':
    init_db()
    print('Base de datos inicializada correctamente.')
