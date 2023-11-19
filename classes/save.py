import json

class SaveManager():
    def __init__(self,path,key) -> None:
        self.path = path
        self.key = key
    
    def encrypt(self) -> bytes:
        pass
    
    def decrypt(self) -> bytes:
        pass
    
    def save(self,value,key):
        self.decrypt()
        try:
            with open(self.path, 'rb') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[key] = value

        with open(self.path, 'wb') as file:
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
        
x = SaveManager('test.save',b"4XLvJ06F6OriXAYLUUjBzkS--AISlUp8P1V2b4QzKA0=")
print(x.load('hu'))
