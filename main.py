import argparse
from contact import Contact
from user import User
from contact_manager import ContactManager
from admin import Admin


def register_admin():
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")
    admin_email = input("Enter admin email: ")
    admin = Admin(admin_username, admin_password, admin_email)
    contact_manager.add_admin(admin)
    print("Admin registered successfully!")


def login_admin():
    admin_username = input("Enter Admin username: ")
    admin_password = input("Enter Admin password: ")
    if contact_manager.authenticate_admin(admin_username, admin_password):
        print("Login successful!")
        return admin_username
    else:
        print("Invalid Admin username or password!")
        return None


def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    user = User(username, password, email)
    contact_manager.add_user(user)
    print("User registered successfully!")


def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if contact_manager.authenticate_user(username, password):
        print("Login successful!")
        return username
    else:
        print("Invalid username or password!")
        return None


def edit_user():
    old_user = input("Enter user's name to edit: ")
    new_user = input("Enter new user: ")
    new_email = input("Enter new email: ")
    new_user = User(new_user, new_email)
    contact_manager.edit_user(old_user, new_user)
    print("Contact edited successfully!")


def delete_user():
    username = input("Enter username to delete: ")
    ContactManager.delete_user(username)
    print(f"User '{username}' deleted successfully!")


def view_users():
    users = contact_manager.view_all_users()
    if users:
        for user in users:
            print(user)
    else:
        print("No users available.")


def add_contact():
    name = input("Enter contact's name: ")
    email = input("Enter contact's email: ")
    phone = input("Enter contact's phone number: ")
    address = input("Enter contact's address: ")
    mobile = input("Enter contact's mobile: ")
    contact = Contact(name, email, phone, mobile, address)
    contact_manager.add_contact(contact)
    print("Contact added successfully!")


def edit_contact():
    old_name = input("Enter contact's name to edit: ")
    new_name = input("Enter new name: ")
    new_email = input("Enter new email: ")
    new_phone = input("Enter new phone number: ")
    new_address = input("Enter new address: ")
    new_mobile = input("Enter new mobile: ")
    new_contact = Contact(new_name, new_email, new_phone, new_mobile, new_address)
    contact_manager.edit_contact(old_name, new_contact)
    print("Contact edited successfully!")


def delete_contact():
    name = input("Enter contact's name to delete: ")
    contact_manager.delete_contact(name)
    print("Contact deleted successfully!")


def view_contacts():
    contacts = contact_manager.view_all_contacts()
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts available.")


def search_contacts(choice):
    field = input(f"Enter {choice} to search: ")
    matching_contacts = contact_manager.search_contacts(field, choice)
    if matching_contacts:
        print("Matching contacts:")
        for contact in matching_contacts:
            print(contact)
    else:
        print("No matching contacts found.")


parser = argparse.ArgumentParser()
parser.add_argument("--admins-file", help="File to load/save admins", default="admins.pkl")
parser.add_argument("--contacts-file", help="File to load/save contacts", default="contacts.pkl")
parser.add_argument("--users-file", help="File to load/save users", default="users.pkl")
parser.add_argument("--register-user", help="Register a new user")
parser.add_argument("--login-user", help="Login with username and password")
parser.add_argument("--add-contact", help="Add a new contact")
parser.add_argument("--edit-contact", help="Edit an existing contact")
parser.add_argument("--delete-contact", help="Delete a contact")
parser.add_argument("--view-contacts", help="View all contacts")
parser.add_argument("--search-name", help="Search contacts by name")
parser.add_argument("--search-email", help="Search contacts by email")
parser.add_argument("--search-phone", help="Search contacts by phone number")
parser.add_argument("--add-user", help="Add a new user (admin only)")
parser.add_argument("--delete-user", help="Delete a user (admin only)")
parser.add_argument("--register-admin", help="Register the admin")
parser.add_argument("--login-admin", help="Login the admin")
args = parser.parse_args()

contact_manager = ContactManager()
contact_manager.load_contacts_from_file(args.contacts_file)
contact_manager.load_users_from_file(args.users_file)
contact_manager.load_admins_from_file(args.admins_file)

if args.register_admin:
    register_admin()
    contact_manager.save_admins_to_file(args.admins_file)
elif args.login_admin:
    contact_manager.load_admins_from_file(args.admins_file)
    admin_check = login_admin()
    if admin_check:
        while True:
            action = input("Choose an action (addUser/editUser/deleteUser/viewUser/\
addContact/editContact/deleteContact/viewContact/quit): ")
            if action == "addUser":
                register_user()
            elif action == "editUser":
                edit_user()
            elif action == "deleteUser":
                delete_user()
            elif action == "viewUser":
                view_users()
            elif action == "addContact":
                add_contact()
            elif action == "editContact":
                edit_contact()
            elif action == "deleteContact":
                delete_contact()
            elif action == "viewContact":
                view_contacts()
            elif action == "quit":
                contact_manager.save_users_to_file(args.users_file)
                contact_manager.save_contacts_to_file(args.contacts_file)
                break
            else:
                print("Only admin users can perform this action.")
elif args.register_user:
    register_user()
    contact_manager.save_users_to_file(args.users_file)
elif args.login_user:
    contact_manager.load_users_from_file(args.users_file)
    username = login_user()
    if username:
        while True:
            action = input("Choose an action (add/edit/delete/view/quit): ").lower()
            if action == "add":
                add_contact()
            elif action == "edit":
                edit_contact()
            elif action == "delete":
                delete_contact()
            elif action == "view":
                view_contacts()
            elif action == "quit":
                contact_manager.save_contacts_to_file(args.contacts_file)
                break
            else:
                print("Invalid choice. Please try again.")
elif args.search_name:
    search_contacts("name")
elif args.search_email:
    search_contacts("email")
elif args.search_phone:
    search_contacts("phone")
else:
    print("No valid option selected.")
