# My Flask Application

## Overview
This Flask application demonstrates basic CRUD operations on a PostgreSQL database, managing a simple Basketball player roster.

## Features
- **Hello World**: Basic test to ensure the application is running.
- **Database Test**: Checks database connectivity.
- **Create Table**: Initializes the database with a required table for storing data.
- **Insert Data**: Populates the table with sample data.
- **Select Data**: Retrieves and displays data from the database.
- **Drop Table**: Cleans up by dropping the table.

## Installation
1. Clone the repository:

``` 
git clone https://github.com/JPFerzacca/flask-hello-world.git
```
* It is reccomended that you make your own branch

2. Install required packages:
```
pip install -r requirements.txt
```


## How to Use
To run the application, execute:

Navigate to `localhost:5000` in your web browser to access the application routes.

## Application Routes
- `/` - Returns a simple "Hello, World!" message.
- `/db_test` - Tests the database connection.
- `/db_create` - Creates a database table.
- `/db_insert` - Inserts predefined data into the database.
- `/db_select` - Displays data from the database in an HTML table.
- `/db_drop` - Drops the database table.

## Dependencies
- Flask
- psycopg2

## Author
JonPaul Ferzacca
