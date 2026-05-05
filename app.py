from flask import Flask, render_template

# instantiate a Flask app object
app = Flask(__name__)

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
    return [
  {
    "title": "The Gruffalo",
    "author": "Julia Donaldson"
  },
  {
    "title": "Ada Twist, Scientist",
    "author": "Andrea Beaty"
  },
  {
    "title": "The Girl Who Drank the Moon",
    "author": "Kelly Barnhill"
  },
  {
    "title": "Dragons in a Bag",
    "author": "Zetta Elliott"
  }
]

@app.route('/authors', methods=['GET'])
def authors():
    return [
        {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
  },
  {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
  },
  {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
  },
  {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
  }
    ]



# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(port=5001, debug=True)
