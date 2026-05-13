from lib.user import User

class UserRepository():
    
    def __init__(self, connection):
        self.connection = connection

    def return_all_users(self):
        """
        returns all users from the db as User instances
        """
        return [
            User(user['username'], user['password'], user['id'])
            for user in self.connection.execute('SELECT * FROM users;')
            ]
    
    def add_new_user(self, user):
        """
        adds new User instance to the users db
        """
        self.connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)',
                                [user.username, user.password])
        return None
    
    def find_user(self, user):
        """
        returns a User instance when the username is provided
        """
        user_details = self.connection.execute('SELECT * FROM users WHERE username=%s', [user])[0]
        return User(
            user_details['username'],
            user_details['password'],
            user_details['id'],
        )
