from lib.book import Book

"""
test book class contructs an instance correctly"""
def test_book_constructs():
    book = Book(1, 'Test title', 'Test author')
    assert book.id == 1
    assert book.title == 'Test title'
    assert book.author == 'Test author'

"""
test str() returns a nicely formatted string of an instance of book
"""
def test_book_formats_nicely():
    book = Book(1, 'Test title', 'Test author')
    assert str(book) == 'Book(1, Test title, Test author)'

"""test two identical instances of book can be compared 
and are considered equal
"""
def test_two_instances_compare():
    book = Book(1, 'Test title', 'Test author')
    book1 = Book(1, 'Test title', 'Test author')
    assert book == book1