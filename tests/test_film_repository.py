from lib.film_repository import FilmRepository
from lib.film import Film

# Test all returns film
def test_get_all_returns_list(db_connection):
    db_connection.seed('seeds/films.sql')
    repo = FilmRepository(db_connection)
    films = repo.all()
    assert films == [
                Film('Dune Part I', 2021, 1),
                Film('Dune Part II', 2024, 2),
                Film('Serenity', 2005, 3),
    ]

def test_adding_film(db_connection):
    db_connection.seed('seeds/films.sql')
    repo = FilmRepository(db_connection)
    new_film = Film(title="A Complete Unknown", release_year=2024)
    repo.add(new_film)
    result = repo.all()
    assert result[-1].title == new_film.title
    assert result[-1].release_year == new_film.release_year