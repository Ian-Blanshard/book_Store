import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

def test_create_user_is_saved_to_database(db_connection):
    db_connection.seed('seeds/user_seeds.sql')
    client = app.test_client()
    response = client.post('/users', data={
        'username': 'testuser1',
        'password': 'password123'
    })
    assert response.status_code == 302
    result = db_connection.execute("SELECT * FROM users WHERE username = 'testuser1'")
    assert len(result) == 1
    assert result[0]['username'] == 'testuser1'

