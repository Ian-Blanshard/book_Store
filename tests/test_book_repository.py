from lib.book import Book
from lib.book_repository import BookRepository

"""
test that all() returns all the book objects
from the seed file
"""
def test_all_returns_all_books(db_connection):
    db_connection.seed('seeds/books_seed.sql')
    repository = BookRepository(db_connection)
    books = repository.all()
    assert books == [
            Book('The Gruffalo', 'Julia Donaldson', 1),
            Book('Ada Twist, Scientist', 'Andrea Beaty', 2),
            Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 3),
            Book('Dragons in a Bag', 'Zetta Elliott', 4),
    ]

"""
test that add_book() correctly adds a new instance of book to the 
database
"""
def test_add_book(db_connection):
    db_connection.seed('seeds/books_seed.sql')
    repository = BookRepository(db_connection)
    book = Book('Leviathan Wakes', 'James S. A. Corey', 5)
    repository.add_book(book)
    books = repository.all()
    assert books == [
            Book('The Gruffalo', 'Julia Donaldson', 1),
            Book('Ada Twist, Scientist', 'Andrea Beaty', 2),
            Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 3),
            Book('Dragons in a Bag', 'Zetta Elliott', 4),
            Book('Leviathan Wakes', 'James S. A. Corey', 5),
    ]
