from lib.user_repository import UserRepository
from lib.user import User
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app


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

"""
tests that a user can login to the system
"""
def test_login_for_auth(db_connection):
    db_connection.seed('seeds/user_seeds.sql')
    client = app.test_client()
    repository = UserRepository(db_connection)
    user = User('testuser2', 'testpassword2', 2)
    repository.add_new_user(user)
    response = client.post('/sessions', data = {
        'username' : 'testuser2', 'password' : 'testpassword2'
        })
    assert response.headers['Location'] == '/'

"""
tests that a unsuccesful login attempt performs as expected
"""
def test_user_failed_login_responds_correctly_incorrect_password(db_connection):
    db_connection.seed('seeds/user_seeds.sql')
    client = app.test_client()
    repository = UserRepository(db_connection)
    user = User('testuser2', 'testpassword2', 2)
    repository.add_new_user(user)
    response = client.post('/sessions', data = {
        'username' : 'testuser2', 'password' : 'wrongpassword'
        })
    assert response.headers['Location'] == 'sessions/new'

def test_user_failed_login_responds_correctly_incorrect_username(db_connection):
    db_connection.seed('seeds/user_seeds.sql')
    client = app.test_client()
    repository = UserRepository(db_connection)
    user = User('testuser2', 'testpassword2', 2)
    repository.add_new_user(user)
    response = client.post('/sessions', data = {
        'username' : 'nottestuser', 'password' : 'wrongpassword'
        })
    assert response.headers['Location'] == 'sessions/new'