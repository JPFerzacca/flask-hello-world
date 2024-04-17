"""
File: app.py
Author: JonPaul Ferzacca
Date: April 16, 2024
Description: This file initializes the Flask application and includes route definitions. It's the main entry point of the application.
Version: 1.0
"""

import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    """
    A simple route to return the 'Hello, World!' string.
    This is typically used as a basic connectivity test.

    Returns:
        str: A greeting string.
    """

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://jp_database_user:ovnfl8P6VnViyPXl9Lp4fvFDP7cjuUot@dpg-co5piv63e1ms73b9oca0-a/jp_database")
    conn.close()
    return "Database Connection Successful"
    """
    Tests the database connectivity using a PostgreSQL connection.
    Closes the connection immediately after opening it.

    Returns:
        str: A message indicating the status of the database connection.
    """

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
    """
    Creates a table in the PostgreSQL database for storing basketball player data.
    Ensures the table does not exist before creating it.

    Returns:
        str: A message confirming the creation of the table.
    """


@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://jp_database_user:ovnfl8P6VnViyPXl9Lp4fvFDP7cjuUot@dpg-co5piv63e1ms73b9oca0-a/jp_database")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"
    """
    Inserts predefined entries of basketball players into the 'Basketball' table.
    Each entry includes the player's first and last name, city, team name, and jersey number.

    Returns:
        str: A message indicating that the data was successfully inserted.
    """

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://jp_database_user:ovnfl8P6VnViyPXl9Lp4fvFDP7cjuUot@dpg-co5piv63e1ms73b9oca0-a/jp_database")
    cur = conn.cursor()
    cur.execute('''
                SELECT * FROM Basketball;
                ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="<tr>"
    response_string+="<td>"
    return response_string
    """
    Fetches all entries from the 'Basketball' table in the database.
    Formats and returns the data in a simple HTML table.

    Returns:
        str: An HTML string representing a table with player data.
    """

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://jp_database_user:ovnfl8P6VnViyPXl9Lp4fvFDP7cjuUot@dpg-co5piv63e1ms73b9oca0-a/jp_database")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
    """
    Drops the 'Basketball' table from the database.
    Used for cleaning up or resetting the database structure.

    Returns:
        str: A message confirming the deletion of the table.
    """
