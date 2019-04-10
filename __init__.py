from flask import Flask, request
from psycopg2 import connect, OperationalError, Error

username = "postgres"
passwd = "coderslab"
hostname = "127.0.0.1"
db_name = "cinemas_db"

def connect_cinemas_db():
    try:
        connection = connect(user=username, password=passwd, host=hostname, database=db_name)
        connection.autocommit = True
    except OperationalError as e:
        print(e)
    except psycopg2.Error as e:
        print(e)
    return connection

def add_movie(name, desc, rating):
    #TUTAJ DALEJ


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run()