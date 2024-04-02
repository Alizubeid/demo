import encryption_manager

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def authenticate(self, username, password):
        return self.username == username and self.password == password

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"
