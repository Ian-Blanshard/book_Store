from lib.user_repository import UserRepository
from lib.user import User

"""
test all returns all users in db
"""
def test_all_returns_all_users(db_connection):
    db_connection.seed('seeds/user_seeds.sql')
    repository = UserRepository(db_connection)
    users = repository.return_all_users()
    assert users == [
        User('testuser', 'testpassword', 1)
    ]    

"""
tests that a new user is succesfully added to the db
"""
def test_add_user(db_connection):
    db_connection.seed('seeds/user_seeds.sql')
    repository = UserRepository(db_connection)
    user = User('testuser2', 'testpassword2', 2)
    repository.add_new_user(user)
    users = repository.return_all_users()
    assert users == [
        User('testuser', 'testpassword', 1),
        User('testuser2', 'testpassword2', 2)
    ]

    

