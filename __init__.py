from flask import Flask, request
from psycopg2 import connect, OperationalError, Error
from elements import navigation, start, end, movie_form, filter_section

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

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return f"""
{start}    
{navigation}
{end}      
"""

@app.route("/cinemas", methods=["GET", "POST"])
def cinemas():
    return f"""
{start}    
{navigation}
{end}      
"""

@app.route("/movies", methods=["GET", "POST"])
def movies():
    if request.method == "GET":
        db_connection = connect_cinemas_db()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT * FROM movie ORDER BY name")
        movie_data = [f"<tr><td>{name}</td><td>{description}</td><td>{rating}</td><td><form action='/movies' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-primary' type='submit' value='Delete'></form></td></tr>" for (id, name, description, rating) in cursor]
        
        return f"""
{start}    
{navigation}
{movie_form}
{filter_section}
<table class='table table-striped'>
    <thead>
    <tr>
        <th>Title</th>
        <th style="width:60%">Description</th>
        <th>Rating</th>
        <th></th>
    </tr>
    </thead>
    <tbody>
    {''.join(movie_data)}
    </tbody>
</table>
{end}      
"""
    if request.method == "POST":
        sql = f"""INSERT INTO movie(name, description, rating) VALUES('{request.form.get("name")}', '{request.form.get("description")}', '{request.form.get("rating")}');"""
        db_connection = connect_cinemas_db()
        cursor = db_connection.cursor()
        if request.form.get("to_delete"):
            cursor.execute(f"DELETE FROM movie WHERE id={request.form.get('to_delete')}")
            filtering = "ORDER BY name"
        if request.form.get("name"):
            cursor.execute(sql)
            filtering = "ORDER BY name"
        if request.form.get("sortby") == "name":
            filtering = "ORDER BY name"
        if request.form.get("sortby") == "ratedesc":
            filtering = "ORDER BY rating DESC"
        if not request.form.get("sortby"):
            filtering = "ORDER BY name"
        cursor.execute(f"SELECT * FROM movie {filtering}")
        movie_data = [f"<tr><td>{name}</td><td>{description}</td><td>{rating}</td><td><form action='/movies' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-primary' type='submit' value='Delete'></form></td></tr>" for (id, name, description, rating) in cursor]
        cursor.close()

        return f"""
{start}    
{navigation}
{movie_form}
{filter_section}
<table class='table table-striped'>
    <thead>
      <tr>
        <th>Title</th>
        <th style="width:60%">Description</th>
        <th>Rating</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      {''.join(movie_data)}
    </tbody>
</table>
{end}      
"""
    

@app.route("/tickets", methods=["GET", "POST"])
def tickets():
    return f"""
{start}    
{navigation}
{end}      
"""

@app.route("/payments", methods=["GET", "POST"])
def payments():
    return f"""
{start}    
{navigation}
{end}      
"""

if __name__ == "__main__":
    app.run(debug=True)