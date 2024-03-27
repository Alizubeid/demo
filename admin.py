from user import User
from contact_manager import ContactManager


class Admin(User):
    def __init__(self, username, password, email):
        super().__init__(username, password, email)

    def add_user(self, user):
        ContactManager.add_user(user)

    def delete_user(self, user):
        ContactManager.delete_user(user)
