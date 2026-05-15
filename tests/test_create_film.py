from app import app
from lib.film import Film
from lib.film_repository import FilmRepository
from flask import session

def test_creating_film_by_a_route(db_connection, logged_in_client):
    db_connection.seed("seeds/films.sql")
    response = logged_in_client.post('/new_film', 
                            data= {
                                'title': 'A Complete Unknown',
                                'release_year': 2024,
                            })
    result = FilmRepository(db_connection).all()
    assert response.status_code == 302
    assert len(result) == 4
    assert result[-1] == Film('A Complete Unknown', 2024, 4)

