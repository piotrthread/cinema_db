navigation = """
<nav class="navbar navbar-expand-sm bg-primary navbar-dark">
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

start = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
        <link rel="stylesheet" href="static/style.css">
        <title>Cinemas_DB</title>
    </head>
    <body>
"""

end = """
    <script src="http://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
    </body>
</html>
"""

movie_form = """
<header id="home-section" class="bg-dark">
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
filter_section = """
<div class="container d-flex justify-content-center">
<form action="/movies" method="POST" class="p-3">
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
"""
