import json
from cryptography.fernet import Fernet

class SaveManager():
    def __init__(self,path,key="Frostlight") -> None:
        self.path = path
        self.key = key

    def encrypt(self, data):
        chipher = Fernet(self.key)
        encrypted_data = chipher.encrypt(data.encode())
        return encrypted_data
    
    def decrypt(self, data):
        chipher = Fernet(self.key)
        decrypted_data = chipher.decrypt(data).decode()
        return decrypted_data
    
    def save(self,value,key):
        try:
            with open(self.path, '+r') as file:
                data = json.loads(self.decrypt(file.read()))
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data[key] = value
        json_string = json.dumps(data)

        with open(self.path, 'w') as file:
            file.write(self.encrypt(json_string))

    def load(self,key) -> any:
        with open(self.path,"r") as file: 
            data = json.load(file)
            if key in data:
                return data[key]
            else:
                return None