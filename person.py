import bcrypt
from index import add_new_data

class Person:

    def __init__(self, n, s, p):
        self.name = n
        self.surname = s
        self.password = p

        add_new_data(self.name, self.surname, self.password)


