from lib.book import Book

class BookRepository():

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        """
        returns all rows from the books table as a list of instances of books
        """
        return [
            Book(row['id'], row['title'], row['author'])
            for row in self.connection.execute('SELECT * FROM books')
        ]