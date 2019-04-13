start = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
        <title>Cinemas_DB</title>
        <style>
        .bg-pink{
            background-color: #FF7DE4;
        }
        .text-pink{
            color: #FF7DE4;
        }
        .top-line{
            border-top:2px solid white;
        }
        </style>
    </head>
    <body class="bg-dark">
"""

navigation = """
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <div class="container">
        <a href="http://localhost:5000/" class="navbar-brand">Cinemas_DB</a>
        <button class="navbar-toggler" data-toggle="collapse" data-target="#menu">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="menu">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a href="http://localhost:5000/cinemas" class="nav-link">Cinemas</a>
                </li>
                <li class="nav-item">
                    <a href="http://localhost:5000/movies" class="nav-link">Movies</a>
                </li>
                <li class="nav-item">
                    <a href="http://localhost:5000/tickets" class="nav-link">Tickets</a>
                </li>
                <li class="nav-item">
                    <a href="http://localhost:5000/payments" class="nav-link">Payments</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
"""

main_menu = """
<div class="container d-flex justify-content-between align-items-center" style='height:100vh;'>
    <h1 class="h-2 p-3"><a href="/cinemas" class="badge badge-warning">CINEMAS</a></h1>
    <h1 class="h-2 p-3"><a href="/movies" class="badge badge-primary">MOVIES</a></h1>
    <h1 class="h-2 p-3"><a href="/tickets" class="badge badge-success">TICKETS</a></h1>
    <h1 class="h-2 p-3"><a href="/payments" class="badge badge-danger">PAYMENTS</a></h1>
</div>
"""

movie_form = """
<header id="home-section" class="bg-dark border-primary border-top">
    <div class="dark-overlay">
        <div class="home-inner container">
            <div class="row d-flex align-items-center bg-dark text-light p-5">
                <div class="col-lg-8 d-none d-lg-block">
                    <h1 class="display-5"><strong>Add, Remove & Filter</strong> Movies.</h1>
                </div>
                <div class="col-lg-4">
                    <div class="card bg-primary text-center card-form">
                        <div class="card-body">
                            <h3>Add Movie</h3>
                            <p>Place your favourite title!</p>
                            <form action="/movies" method="POST">
                                <div class="form-group">
                                    <input type="text" class="form-control form-control-lg" placeholder="Title" name="name">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control form-control-lg" placeholder="Description" name="description">
                                </div>
                                <div class="form-group">
                                    <label>Rating:</label>
                                    <select class="form-control" name="rating">
                                    <option>0</option>
                                    <option>1</option>
                                    <option>2</option>
                                    <option>3</option>
                                    <option>4</option>
                                    <option>5</option>
                                    <option>6</option>
                                    <option>7</option>
                                    <option>8</option>
                                    <option>9</option>
                                    <option>10</option>
                                </select>
                                </div>
                                 <input type="submit" value="Submit" class="btn btn-outline-light btn-block">
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>
"""

filter_section_movie = """
<section class="bg-light">
    <div class="container d-flex justify-content-center text-dark bg-light">
        <form action="/movies" method="POST" class="pb-3">
            <div class="form-check-inline">
                <label class="form-check-label mx-5">
                Sort By: 
                </label>
                <label class="form-check-label">
                    <input type="radio" class="form-check-input" name="sortby" value="name">Name
                </label>
            </div>
            <div class="form-check-inline">
                <label class="form-check-label">
                    <input type="radio" class="form-check-input" name="sortby" value="ratedesc">Rating
                </label>
            </div>
            <input type="submit" class="btn btn-outline-primary mx-5" value="Sort">
        </form>
    </div>
</section>
"""
cinema_form = """
<header id="home-section" class="bg-dark border-warning border-top">
    <div class="dark-overlay">
        <div class="home-inner container">
            <div class="row d-flex align-items-center bg-dark text-light p-5">
                <div class="col-lg-8 d-none d-lg-block">
                    <h1 class="display-5"><strong>Add, Remove & Search</strong> Cinemas.</h1>
                </div>
                <div class="col-lg-4">
                    <div class="card bg-warning text-center card-form">
                        <div class="card-body text-dark">
                            <h3>Add Cinema</h3>
                            <p>Post your favourite place!</p>
                            <form action="/cinemas" method="POST">
                                <div class="form-group">
                                    <input type="text" class="form-control form-control-lg" placeholder="Name" name="name">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control form-control-lg" placeholder="Adress" name="adress">
                                </div>
                                 <input type="submit" value="Submit" class="btn btn-outline-dark btn-block">
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>
"""
filter_section_cinema = """
<section class="bg-light">
    <div class="text-dark bg-light container">
        <form action="/cinemas" method="POST" class="p-3">
            <div class="form-row">
                <i class="fas fa-search mx-3 py-2"></i>
                <div class="col">
                    <input type="text" class="form-control" name="search" placeholder="Search cinemas...">
                </div>
                <input type="submit" class="btn btn-outline-dark mx-5" value="Search">
            </div>
        </form>
    </div>
</section>
"""
search_section_movie = """
<section class="bg-light">
    <div class="text-dark bg-light container">
        <form action="/movies" method="POST" class="p-3">
            <div class="form-row">
                <i class="fas fa-search mx-3 py-2"></i>
                <div class="col">
                    <input type="text" class="form-control" name="search" placeholder="Search movies...">
                </div>
                <input type="submit" class="btn btn-outline-primary mx-5" value="Search">
            </div>
        </form>
    </div>
</section>
"""
ticket_form = """
<header id="home-section" class="bg-dark border-success border-top">
    <div class="dark-overlay">
        <div class="home-inner container">
            <div class="row d-flex align-items-center bg-dark text-light p-5">
                <div class="col-lg-8 d-none d-lg-block">
                    <h1 class="display-5"><strong>Add & Remove</strong> Tickets.</h1>
                </div>
                <div class="col-lg-4">
                    <div class="card bg-success text-center card-form">
                        <div class="card-body text-dark">
                            <h3>Add Ticket</h3>
                            <p>Put tickets to buy!</p>
                            <form action="/tickets" method="POST">
                                <div class="form-group">
                                    <input type="number" class="form-control form-control-lg" placeholder="Qty" name="quantity">
                                </div>
                                <div class="form-group">
                                    <select class="form-control" name="price">
                                        <option value="9.50">Adult - 9.50$</option>
                                        <option value="7.50">Student - 7.50$</option>
                                        <option value="6.75">Club Ticket - 6.75$</option>
                                    </select>
                                </div>
                                 <input type="submit" value="Submit" class="btn btn-outline-dark btn-block">
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>
"""

payment_form = """
<header id="home-section" class="bg-dark border-danger border-top">
    <div class="dark-overlay">
        <div class="home-inner container">
            <div class="row d-flex align-items-center bg-dark text-light p-5">
                <div class="col-lg-8 d-none d-lg-block">
                    <h1 class="display-5"><strong>Add, Remove & Filter</strong> Payments.</h1>
                </div>
                <div class="col-lg-4">
                    <div class="card bg-danger text-center card-form">
                        <div class="card-body">
                            <h3>Add Payment</h3>
                            <p>Make new payment!</p>
                            <form action="/payments" method="POST">
                                <div class="form-group">
                                    <label>Choose payment:</label>
                                    <select class="form-control" name="pay_type">
                                        <option value="Bank Transfer">Transfer</option>
                                        <option value="Credit Card">Credit Card</option>
                                        <option value="Pay-Pal">Pay-Pal</option>
                                        <option value="BLIK">BLIK</option>
                                    </select>
                                </div>
                                <div class="form-group">
                                    <input type="number" class="form-control form-control-lg" placeholder="Amount: $" name="amount">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control form-control-lg" placeholder="Date: MM-DD-YY" name="date">
                                </div>
                                 <input type="submit" value="Submit" class="btn btn-outline-light btn-block">
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>
"""

filter_section_payment = """
<section class="bg-light">
    <div class="container d-flex justify-content-center text-dark bg-light">
        <form action="/movies" method="POST" class="pb-3">
            <div class="form-check-inline">
                <label class="form-check-label mx-5">
                Sort By: 
                </label>
                <label class="form-check-label">
                    <input type="radio" class="form-check-input" name="sortby" value="name">Name
                </label>
            </div>
            <div class="form-check-inline">
                <label class="form-check-label">
                    <input type="radio" class="form-check-input" name="sortby" value="ratedesc">Rating
                </label>
            </div>
            <input type="submit" class="btn btn-outline-primary mx-5" value="Sort">
        </form>
    </div>
</section>
"""

search_section_payment = """
<section class="bg-light">
    <div class="text-dark bg-light">
        <form action="/payments" method="POST" class="p-3 container">
                <div class="form-row">
                    <div class="col-1 d-flex align-items-center justify-content-end">
                        <i class="fas fa-search"></i>
                    </div>
                    <div class="col">
                        <input type="text" class="form-control" name="search" placeholder="Search date: MM-DD-YY">
                    </div>
                    <div class="col-3 d-flex align-items-center justify-content-around">
                        <div class="form-check-inline mx-2">
                            <input type="radio" class="form-check-input mx-2" name="sortby" value="before"><label class="form-check-label mr-5">Before</label>
                            <input type="radio" class="form-check-input mx-2" name="sortby" value="after"><label class="form-check-label">After</label>
                        </div>
                    </div>
                    <div class="col-2">
                        <input type="submit" class="btn btn-outline-danger" value="Search">
                    </div>
                </div>
                
        </form>
    </div>
</section>
"""


end = """
    <script src="http://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
    </body>
</html>
"""