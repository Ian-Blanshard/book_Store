from lib.film import Film
class FilmRepository():

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        return [Film(title=film["title"], release_year=film["release_year"], id=film["id"])
                 for film in self._connection.execute('SELECT * FROM films')]
    
    def add(self, film):
        self._connection.execute("INSERT INTO films (title, release_year) VALUES (%s, %s)", [film.title, film.release_year])
        return None