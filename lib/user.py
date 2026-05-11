class User():
    
    def __init__(self, username, password, id = None):
        self.username = username
        self.password = password
        self.id = id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'User({self.username}, {self.password}, {self.id})'