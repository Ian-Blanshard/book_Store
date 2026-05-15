from flask import Flask, render_template, request, redirect, session
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.user_repository import UserRepository
from lib.film_repository import FilmRepository
from lib.authenticated import is_authenticated
from lib.book import Book
from lib.user import User
from lib.film import Film
from lib.login_required import login_required

# instantiate a Flask app object
app = Flask(__name__, static_folder='static')
app.secret_key = "some_really_secret_key"

# ========================================================================== #
# ======================= GENERAL PAGES ROUTES ============================= #
# ========================================================================== #

# app routes
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/authors', methods=['GET'])
def authors():
    return render_template('authors.html')

# ========================================================================== #
# ================================ BOOK ROUTES ============================= #
# ========================================================================== #

@app.route('/books', methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    repository = BookRepository(connection).all()
    return render_template("books.html", books= repository)

@app.route('/new_book', methods=['GET'])
@login_required
def add_book_form():
    return render_template('add_new_book.html')

@app.route('/new_book', methods=['POST'])
@login_required
def add_book_to_database():
    connection = DatabaseConnection()
    connection.connect()
    data = request.form
    repository = BookRepository(connection)
    repository.add_book(Book(data['title'], data['author']))
    return redirect('/books')

# ========================================================================== #
# =============================== FILMS ROUTES ============================= #
# ========================================================================== #

@app.route('/films', methods=['GET'])
def get_all_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

@app.route('/new_film', methods=['GET'])
@login_required
def add_film_form():
    return render_template('add_new_film.html')

@app.route('/new_film', methods=["POST"])
@login_required
def create_new_film():
    connection = DatabaseConnection()
    connection.connect()
    repo = FilmRepository(connection)
    film = request.form
    repo.add(Film(title=film['title'], release_year=film['release_year']))
    return redirect('/films')

# ========================================================================== #
# ========================== USER/LOGIN ROUTES ============================= #
# ========================================================================== #

@app.route('/users', methods=['GET'])
def get_user_form():
    return render_template('signup_form.html')

@app.route('/users', methods=['POST'])
def add_user():
    connection = DatabaseConnection()
    connection.connect()
    data = request.form
    repository = UserRepository(connection)
    repository.add_new_user(User(data['username'], data['password']))
    return redirect('/')

@app.route('/sessions/new', methods=['GET'])
def show_login_form():
    return render_template('login_form.html')

@app.route('/sessions', methods=['POST'])
def submit_login_form():
    connection = DatabaseConnection()
    connection.connect()
    repository = UserRepository(connection)
    username, password = request.form['username'], request.form['password']
    user = repository.find_user(username)
    if user:
        if password == user.password:
            session['username'] = user.username
            session['user_id'] = user.id
            return redirect('/')
        else:
            return redirect('sessions/new') 
    else:
        return redirect('sessions/new')
    
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)