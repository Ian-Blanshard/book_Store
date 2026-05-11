from lib.user import User

def test_user_constructs():
    user = User('Test username', 'Test password', 1)
    assert user.username == 'Test username'
    assert user.password == 'Test password'
    assert user.id == 1

def test_two_identical_instances_of_user_are_equal():
    user = User('Test username', 'Test password', 1)
    user1 = User('Test username', 'Test password', 1)
    assert user == user1

def test_user_string():
    user = User('Test username', 'Test password', 1)
    assert str(user) == 'User(Test username, Test password, 1)'