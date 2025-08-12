import sqlite3
from flask import Flask, jsonify, g
import os

DATABASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data', 'mydb.sqlite')
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'schema.sql')
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'db', 'init.sql')


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DATABASE)
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        db.executescript(f.read())
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        db.executescript(f.read())
    db.close()


def create_app():
    app = Flask(__name__)

    @app.before_request
    def before_request():
        get_db()

    @app.teardown_appcontext
    def teardown_db(exception):
        close_db()

    @app.route('/clientes', methods=['GET'])
    def get_clientes():
        db = get_db()
        clientes = db.execute('SELECT id, nombre, email FROM clientes').fetchall()
        return jsonify([dict(row) for row in clientes])
    
    @app.route('/clientes/<int:id_cliente>/compras', methods=['GET'])
    def get_compras_cliente(id_cliente):
        db = get_db()
        compras = db.execute('SELECT id, producto, cantidad FROM compras WHERE cliente_id = ?', (id_cliente,)
        ).fetchall()
        return jsonify([dict(row) for row in compras])

    @app.cli.command('init-db')
    def init_db_command():
        """Inicializa la base de datos."""
        init_db()
        print('Base de datos inicializada.')

    return app
