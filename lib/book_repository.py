from lib.book import Book

class BookRepository():

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        """
        returns all rows from the books table as a list of instances of books
        """
        return [
            Book(row['title'], row['author'], row['id'])
            for row in self.connection.execute('SELECT * FROM books')
        ]
    
    def add_book(self, book):
        """
        adds a new book instance to the database
        """
        self.connection.execute('INSERT INTO books (title, author) VALUES (%s, %s)', 
                                [book.title, book.author])
        return None