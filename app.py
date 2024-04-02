import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://jp_database_user:ovnfl8P6VnViyPXl9Lp4fvFDP7cjuUot@dpg-co5piv63e1ms73b9oca0-a/jp_database")
    conn.close()
    return "Database Connection Successful"