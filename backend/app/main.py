
from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

# Ruta absoluta a la base de datos
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'db', 'data', 'clientes_compras.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/clientes', methods=['GET'])
def get_clientes():
    conn = get_db_connection()
    clientes = conn.execute('SELECT id, nombre, email FROM clientes').fetchall()
    conn.close()
    return jsonify([dict(row) for row in clientes])

# Nuevo endpoint para obtener compras de un cliente por su ID
@app.route('/clientes/<int:id_cliente>/compras', methods=['GET'])
def get_compras_cliente(id_cliente):
    conn = get_db_connection()
    compras = conn.execute('SELECT id, producto, cantidad FROM compras WHERE cliente_id = ?', (id_cliente,)).fetchall()
    conn.close()
    return jsonify([dict(row) for row in compras])

if __name__ == '__main__':
    app.run(debug=True)
