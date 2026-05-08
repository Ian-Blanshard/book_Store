import sys
import os

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_home_returns_a_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_get_books_returns_a_200():
    client = app.test_client()
    response = client.get("/books")
    assert response.status_code == 200

def test_authors_route_returns_200():
    client = app.test_client()
    response = client.get('/authors')
    assert response.status_code == 200

def test_team_route_returns_200():
    client = app.test_client()
    response = client.get('/team')
    assert response.status_code == 200

