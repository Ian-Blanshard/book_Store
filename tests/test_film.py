from lib.film import Film

# 1
# Test Film class
def test_book_assigns_variables():
    film = Film('Dune Part I',2021, 1)
    assert film.id == 1
    assert film.title == 'Dune Part I'
    assert film.release_year == 2021

def test_eq():
    film1 = Film('Dune Part I',2021, 1)
    film2 = Film('Dune Part I',2021, 1)
    assert film1 == film2

def test_repr():
    film = Film('Dune Part I', 2021, 1)
    assert str(film) == 'Film(Dune Part I, 2021, 1)'