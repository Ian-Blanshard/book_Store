# test_create_user.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app
from lib.database_connection import DatabaseConnection

def test_create_user_is_saved_to_database(db_connection):
    db_connection.seed('seeds/user_seeds.sql')
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()

    response = client.post('/users', data={
        'username': 'testuser1',
        'password': 'password123'
    })

    # assert that the redirect happened
    assert response.status_code == 302
    result = connection.execute("SELECT * FROM users WHERE username = 'testuser1'")
    # assert that the user was created
    assert len(result) == 1
    assert result[0]['username'] == 'testuser1'

