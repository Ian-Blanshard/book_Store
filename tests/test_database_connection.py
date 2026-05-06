
def test_database_connection(db_connection):

    db_connection.seed('seeds/books_seed.sql')

    result = db_connection.execute('SELECT * FROM books')

    assert result == [
        {'id': 1, 'title': 'The Gruffalo', 'author': 'Julia Donaldson'},
        {'id': 2, 'title': 'Ada Twist, Scientist', 'author': 'Andrea Beaty'},
        {'id': 3, 'title': 'The Girl Who Drank the Moon', 'author': 'Kelly Barnhill'},
        {'id': 4, 'title': 'Dragons in a Bag', 'author': 'Zetta Elliott'}
    ]