from lib.film_repository import FilmRepository
from lib.film import Film

# 2
# Test all returns film
def test_get_all_returns_list(db_connection):
    db_connection.seed('seeds/films.sql')
    repo = FilmRepository(db_connection)
    films = repo.all()
    print(films[0])
    film_1 = Film('Dune Part I', 2021, 1)
    film_2 = Film('Dune Part II', 2024, 2)
    film_3 = Film('Serenity', 2005, 3)
    assert films[0] == film_1
    assert films[1] == film_2
    assert films[2] == film_3
