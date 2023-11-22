import json
from cryptography.fernet import Fernet

class SaveManager():
    def __init__(self,path="data.save",key=b"z8IwBgA-gFs66DrrM7JHtXe0fl9OVtL3A8Q-xU1nmAA=") -> None:
        self.path = path
        self.key = key
    
    def encrypt(self) -> bytes:
        with open(self.path, 'rb') as file:
            data = file.read()

        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data)

        with open(self.path, 'wb') as file:
            file.write(encrypted_data)
    
    def decrypt(self) -> bytes:
        try:
            with open(self.path, 'rb') as file:
                data = file.read()
            if data != b'':
                fernet = Fernet(self.key)
                decrypted_data = fernet.decrypt(data)

                with open(self.path, 'wb') as file:
                    file.write(decrypted_data)
        except FileNotFoundError:
            pass
    
    def save(self,key,value):
        self.decrypt()
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[key] = value

        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)
        self.encrypt()
    
    def load(self,key) -> any:
        self.decrypt()
        try:
            with open(self.path, 'rb') as file:
                data = json.load(file)
                if key in data:
                    self.encrypt()
                    return data[key]
                else:
                    self.encrypt()
                    return None
        except (FileNotFoundError, json.JSONDecodeError):
            self.encrypt()
            return None