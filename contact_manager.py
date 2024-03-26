import pickle
import re


class ContactManager:
    def __init__(self):
        self.contacts = []
        self.users = []

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

    def add_user(self, user):
        self.users.append(user)

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

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
