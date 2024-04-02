from cryptography.fernet import Fernet 

class EncryptionManager:
    def __init__(self,key = None):
        self.key = Fernet.generate_key() if not key else key
        self.random = Fernet(self.key)

    def encrypt(self,data : str):
        encrypted_data =  self.random.encrypt(data.encode()).decode()
        return encrypted_data
    
    def decrypt(self,data: str):
        decrypted_data = self.random.decrypt(data.encode()).decode()
        return decrypted_data
    
    def key(self):
        return self.key
    

