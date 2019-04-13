from flask import Flask, request
from psycopg2 import connect, OperationalError, Error
from elements import navigation, start, end, movie_form, filter_section_movie, cinema_form, filter_section_cinema, search_section_movie, ticket_form, main_menu, payment_form, search_section_payment

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
    {main_menu}
    {end}      
    """

#------------------------------------------CINEMAS
@app.route("/cinemas", methods=["GET", "POST"])
def cinemas():
    if request.method == "GET":
        db_connection = connect_cinemas_db()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT * FROM cinema ORDER BY name")
        cinema_data = [f"<tr><td></td><td>{name}</td><td>{adress}</td><td><form action='/cinemas' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-warning' type='submit' value='Delete'></form></td><td></td></tr>" for (id, name, adress) in cursor]
        
        return f"""
        {start}    
        {navigation}
        {cinema_form}
        {filter_section_cinema}
            <table class='table table-striped table-dark'>
                <thead>
                <tr class="bg-warning text-dark">
                    <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
                    <th>Name</th>
                    <th style="width:60% text-center">Adress</th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {''.join(cinema_data)}
                </tbody>
            </table>
        {end}      
        """

    if request.method == "POST":
        sql = f"""INSERT INTO cinema(name, adress) VALUES('{request.form.get("name")}', '{request.form.get("adress")}')"""
        db_connection = connect_cinemas_db()
        cursor = db_connection.cursor()

        if request.form.get("to_delete"):
            cursor.execute(f"DELETE FROM cinema WHERE id={request.form.get('to_delete')}")
            filtering = "ORDER BY name"

        if request.form.get("search"):
            filtering = f"WHERE name ILIKE '%{request.form.get('search')}%' OR adress ILIKE '%{request.form.get('search')}%'"

        if not request.form.get("search"):
            filtering = "ORDER BY name"

        if request.form.get("name"):
            cursor.execute(sql)
            filtering = "ORDER BY name"

        cursor.execute(f"SELECT * FROM cinema {filtering}")
        cinema_data = [f"<tr><td></td><td>{name}</td><td>{adress}</td><td><form action='/cinemas' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-warning' type='submit' value='Delete'></form></td><td></td></tr>" for (id, name, adress) in cursor]
        cursor.close()

        return f"""
        {start}    
        {navigation}
        {cinema_form}
        {filter_section_cinema}
            <table class='table table-striped table-dark'>
                <thead>
                <tr class="bg-warning text-dark">
                    <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
                    <th>Name</th>
                    <th style="width:60% text-center">Adress</th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {''.join(cinema_data)}
                </tbody>
            </table>
        {end}      
        """

#------------------------------------------------MOVIES
@app.route("/movies", methods=["GET", "POST"])
def movies():
    if request.method == "GET":
        db_connection = connect_cinemas_db()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT * FROM movie ORDER BY name")
        movie_data = [f"<tr><td></td><td>&nbsp&nbsp&nbsp{name}</td><td>{description}</td><td>&nbsp&nbsp&nbsp{rating}</td><td><form action='/movies' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-primary' type='submit' value='Delete'></form></td><td></td></tr>" for (id, name, description, rating) in cursor]

        return f"""
        {start}    
        {navigation}
        {movie_form}
        {search_section_movie}
        {filter_section_movie}
        <table class='table table-striped table-dark'>
            <thead>
            <tr class="bg-primary text-light">
                <th></th>
                <th>Title</th>
                <th style="width:60%">Description</th>
                <th>Rating</th>
                <th></th>
                <th></th>
            </tr>
            </thead>
            <tbody class="text-light">
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

        if request.form.get("search"):
            filtering = f"WHERE name ILIKE '%{request.form.get('search')}%'"

        if request.form.get("name"):
            cursor.execute(sql)
            filtering = "ORDER BY name"

        if request.form.get("sortby") == "name":
            filtering = "ORDER BY name"

        if request.form.get("sortby") == "ratedesc":
            filtering = "ORDER BY rating DESC"

        if not request.form.get("sortby") and not request.form.get("search"):
            filtering = "ORDER BY name"

        cursor.execute(f"SELECT * FROM movie {filtering}")
        movie_data = [f"<tr><td></td><td>{name}</td><td>{description}</td><td>{rating}</td><td><form action='/movies' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-primary' type='submit' value='Delete'></form></td><td></td></tr>" for (id, name, description, rating) in cursor]
        cursor.close()

        return f"""
        {start}    
        {navigation}
        {movie_form}
        {search_section_movie}
        {filter_section_movie}
        <table class='table table-striped table-dark'>
            <thead>
            <tr class="bg-primary text-light">
                <th></th>
                <th>Title</th>
                <th style="width:60%">Description</th>
                <th>Rating</th>
                <th></th>
                <th></th>
            </tr>
            </thead>
            <tbody class="text-light">
            {''.join(movie_data)}
            </tbody>
        </table>
        {end}      
        """
    
#-------------------------------------TICKETS    
@app.route("/tickets", methods=["GET", "POST"])
def tickets():
    if request.method == "GET":
        db_connection = connect_cinemas_db()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT * FROM ticket ORDER BY id")
        ticket_data = [f"<tr><td></td><td>CIN_NUM_00T_{id}</td><td>{quantity}</td><td>{price*quantity}$</td><td><form action='/tickets' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-success' type='submit' value='Delete'></form></td><td></td></tr>" for (id, quantity, price) in cursor]
        
        return f"""
        {start}    
        {navigation}
        {ticket_form}
            <table class='table table-striped table-dark'>
                <thead>
                <tr class="bg-success text-dark">
                    <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
                    <th>#</th>
                    <th>Qty</th>
                    <th>Price</th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {''.join(ticket_data)}
                </tbody>
            </table>
        {end}      
        """

    if request.method == "POST":
        sql = f"""INSERT INTO ticket(quantity, price) VALUES('{request.form.get("quantity")}', '{request.form.get("price")}')"""
        db_connection = connect_cinemas_db()
        cursor = db_connection.cursor()

        if request.form.get("to_delete"):
            cursor.execute(f"DELETE FROM ticket WHERE id={request.form.get('to_delete')}")
            filtering = "ORDER BY id"

        if request.form.get("quantity"):
            cursor.execute(sql)
            filtering = "ORDER BY id"

        cursor.execute(f"SELECT * FROM ticket {filtering}")
        ticket_data = [f"<tr><td></td><td>&nbsp&nbsp&nbsp&nbsp&nbspCIN_NUM_00T_{id}</td><td>{quantity}</td><td>{price*quantity}$</td><td><form action='/tickets' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-success' type='submit' value='Delete'></form></td><td></td></tr>" for (id, quantity, price) in cursor]
        cursor.close()

        return f"""
        {start}    
        {navigation}
        {ticket_form}
            <table class='table table-striped table-dark'>
                <thead>
                <tr class="bg-success text-dark">
                    <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
                    <th>#</th>
                    <th>Qty</th>
                    <th>Price</th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {''.join(ticket_data)}
                </tbody>
            </table>
        {end}      
        """
#----------------------------------------PAYMENTS
@app.route("/payments", methods=["GET", "POST"])
def payments():
    if request.method == "GET":
        db_connection = connect_cinemas_db()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT * FROM payment ORDER BY date DESC")
        payment_data = [f"<tr><td></td><td>&nbsp&nbsp&nbsp{date}</td><td class='text-center'>{amount}$</td><td>&nbsp&nbsp&nbsp{pay_type}</td><td><form action='/payments' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-danger' type='submit' value='Delete'></form></td><td></td></tr>" for (id, pay_type, amount, date) in cursor]

        return f"""
        {start}    
        {navigation}
        {payment_form}
        {search_section_payment}
        <table class='table table-striped table-dark'>
            <thead>
            <tr class="bg-danger text-light">
                <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
                <th>Date</th>
                <th style="width:30%" class="text-center">Amount</th>
                <th>Payment Type</th>
                <th></th>
                <th></th>
            </tr>
            </thead>
            <tbody class="text-light">
            {''.join(payment_data)}
            </tbody>
        </table>
        {end}      
        """

    if request.method == "POST":
        sql = f"""INSERT INTO payment(type, amount, date) VALUES('{request.form.get("pay_type")}', '{request.form.get("amount")}', '{request.form.get("date")}');"""
        db_connection = connect_cinemas_db()
        cursor = db_connection.cursor()

        if request.form.get("search"):
            filtering = f"WHERE date='{request.form.get('search')}'"

        if not request.form.get("search") and request.form.get("sortby"):
            filtering = "ORDER BY date DESC"

        if request.form.get("search") and request.form.get("sortby"):
            if request.form.get("sortby") == "after":
                filtering = f"WHERE date >= '{request.form.get('search')}' ORDER BY date DESC"
            if request.form.get("sortby") == "before":
                filtering = f"WHERE date <= '{request.form.get('search')}' ORDER BY date DESC"
        
        if not request.form.get("search") and not request.form.get("sortby"):
            filtering = f"ORDER BY date DESC"

        if request.form.get("to_delete"):
            cursor.execute(f"DELETE FROM payment WHERE id={request.form.get('to_delete')}")
            filtering = "ORDER BY date DESC"

        if request.form.get("pay_type"):
            cursor.execute(sql)
            filtering = "ORDER BY date DESC"

        cursor.execute(f"SELECT * FROM payment {filtering}")
        payment_data = [f"<tr><td></td><td>&nbsp&nbsp&nbsp{date}</td><td class='text-center'>{amount}$</td><td>&nbsp&nbsp&nbsp{pay_type}</td><td><form action='/payments' method='POST'><input type='hidden' name='to_delete' value='{id}'><input class='btn btn-outline-danger' type='submit' value='Delete'></form></td><td></td></tr>" for (id, pay_type, amount, date) in cursor]
        cursor.close()

        return f"""
        {start}    
        {navigation}
        {payment_form}
        {search_section_payment}
        <table class='table table-striped table-dark'>
            <thead>
            <tr class="bg-danger text-light">
                <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
                <th>Date</th>
                <th style="width:30%" class="text-center">Amount</th>
                <th>Payment Type</th>
                <th></th>
                <th></th>
            </tr>
            </thead>
            <tbody class="text-light">
            {''.join(payment_data)}
            </tbody>
        </table>
        {end}      
        """

if __name__ == "__main__":
    app.run(debug=True)