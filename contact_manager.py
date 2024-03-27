import pickle
import re


class ContactManager:
    def __init__(self):
        self.contacts = []
        self.users = []
        self.admins = []

    def load_admins_from_file(self, admins_file):
        try:
            with open(admins_file, 'rb') as file:
                self.admins = pickle.load(file)
        except FileNotFoundError:
            print("Admins file not found.")

    def save_admins_to_file(self, admins_file):
        with open(admins_file, 'wb') as file:
            pickle.dump(self.admins, file)

    def load_contacts_from_file(self, contacts_file):
        try:
            with open(contacts_file, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            print("Contacts file not found.")

    def save_contacts_to_file(self, contacts_file):
        with open(contacts_file, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_users_from_file(self, users_file):
        try:
            with open(users_file, 'rb') as file:
                self.users = pickle.load(file)
        except FileNotFoundError:
            print("Users file not found.")

    def save_users_to_file(self, users_file):
        with open(users_file, 'wb') as file:
            pickle.dump(self.users, file)

    def add_admin(self, admin):
        self.admins.append(admin)

    def authenticate_admin(self, admin_username, admin_password):
        for admin in self.admins:
            if admin.username == admin_username and admin.password == admin_password:
                return True
        return False

    def add_user(self, user):
        self.users.append(user)

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

    def edit_user(self, old_user, new_user):
        for i, user in enumerate(self.users):
            if user.name == old_user:
                self.users[i] = new_user
                break

    def delete_user(self, name):
        self.users = [user for user in self.users if user.name != name]

    def view_all_users(self):
        return self.users

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[i] = new_contact
                break

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def view_all_contacts(self):
        return self.contacts

    def search_contacts(self, field, choice):
        matching_contacts = []
        pattern = re.compile(field, re.IGNORECASE)
        for contact in self.contacts:
            if choice == "name" and pattern.search(contact.name):
                matching_contacts.append(contact)
            elif choice == "email" and pattern.search(contact.email):
                matching_contacts.append(contact)
            elif choice == "phone" and pattern.search(contact.phone):
                matching_contacts.append(contact)
        return matching_contacts
