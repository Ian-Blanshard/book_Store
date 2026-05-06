from lib.book import Book
from lib.book_repository import BookRepository

"""
test that all() returns all the book objects
from the seed file
"""
def test_all_returns_all_books(db_connection):
    # seed the database
    db_connection.seed('seeds/books_seed.sql')
    repository = BookRepository(db_connection)

    books = repository.all()

    assert books == [
            Book(1, 'The Gruffalo', 'Julia Donaldson'),
            Book(2, 'Ada Twist, Scientist', 'Andrea Beaty'),
            Book(3, 'The Girl Who Drank the Moon', 'Kelly Barnhill'),
            Book(4, 'Dragons in a Bag', 'Zetta Elliott'),
    ]