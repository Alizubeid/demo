class Contact:
    def __init__(self, name, email, phone, mobile, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.mobile = mobile
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Mobile: {self.mobile}, Address: {self.address}"
