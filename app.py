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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://jp_database_user:ovnfl8P6VnViyPXl9Lp4fvFDP7cjuUot@dpg-co5piv63e1ms73b9oca0-a/jp_database")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

