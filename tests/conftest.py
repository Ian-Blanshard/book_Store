import pytest
from ..lib.database_connection import DatabaseConnection
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    return conn

# create a pytest fixture which can be used to simulate a logged in user. 
@pytest.fixture
def logged_in_client():
    client = app.test_client()
    with client.session_transaction() as current_session:
        current_session['username'] = 'testuser'
        current_session['user_id'] = 1
    yield client
