from flask import Flask, render_template

# instantiate a Flask app object
app = Flask(__name__, static_folder='static')

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

@app.route('/books', methods=['GET'])
def get():
    return render_template("books.html") 


@app.route('/authors', methods=['GET'])
def authors():
    return render_template('authors.html')


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
