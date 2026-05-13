class Film():

    def __init__(self, title, release_year, id = None):
        self.title = title
        self.release_year = release_year
        self.id = id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"Film({self.title}, {self.release_year}, {self.id})"