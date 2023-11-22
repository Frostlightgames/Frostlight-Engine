import os
import json
import shutil
import datetime
from cryptography.fernet import Fernet

class SaveManager():
    def __init__(self,engine,path="data/saves/save") -> None:
        self.engine = engine
        self.path = path
        self.encryption_key = b"z8IwBgA-gFs66DrrM7JHtXe0fl9OVtL3A8Q-xU1nmAA="

    def set_encryption_key(self,encryption_key:bytes) -> None:
        self.encryption_key = encryption_key

    def generate_encryption_key(self) -> bytes:
        return Fernet.generate_key()
    
    def set_save_path(self,path:str) -> None:
        self.path = path
    
    def encrypt(self,data:dict) -> bool:
        try:
            fernet = Fernet(self.encryption_key)
            encrypted_data = fernet.encrypt(bytes(json.dumps(data,ensure_ascii=True).encode("utf-8")))

            with open(self.path, 'wb') as file:
                file.write(encrypted_data)
        except Exception as e:
            self.engine.logger.error(e)
    
    def decrypt(self) -> bool|dict:
        try:
            with open(self.path, 'rb') as file:
                data = file.read()
            if data != b'':
                fernet = Fernet(self.encryption_key)
                return json.loads(fernet.decrypt(data))
            
        except Exception as e:
            self.engine.logger.error(e)

        return False
    
    def save(self,key,value) -> bool:
        try:
            data = self.decrypt()
            if data != False:
                data[key] = value
            else:
                data = {}
            self.encrypt(data)
            return True
        except Exception as e:
            self.engine.logger.error(e)

        return False
    
    def load(self,key) -> any:
        if os.path.exists(self.path):
            try:
                data = self.decrypt()
                if data != False:
                    return data[key]
            except Exception as e:
                self.engine.logger.error(e)
        else:
            return None
        
    def backup(self,backup_path:str="data/saves/backup"):
        shutil.copyfile(self.path,os.path.join(backup_path,f'{os.path.split(self.path)[-1]}-{datetime.datetime.now().strftime("%H-%M-%S")}'))