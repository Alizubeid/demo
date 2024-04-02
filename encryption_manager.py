from cryptography.fernet import Fernet
import pickle

class EncryptionManager:
    def __init__(self, key_file):
        self.key_file = key_file
        self.load_key()

    def load_key(self):
        try:
            with open(self.key_file, 'rb') as file:
                self.key = file.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(self.key)

    def encrypt(self, data):
        cipher_suite = Fernet(self.key)
        encrypted_data = cipher_suite.encrypt(pickle.dumps(data))
        return encrypted_data

    def decrypt(self, encrypted_data):
        cipher_suite = Fernet(self.key)
        decrypted_data = pickle.loads(cipher_suite.decrypt(encrypted_data))
        return decrypted_data

