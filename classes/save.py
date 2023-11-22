import os
import json
import shutil
import datetime
from cryptography.fernet import Fernet

class SaveManager():
    def __init__(self,engine,path="data/saves/save") -> None:
        """
        Initialize the SaveManager object.

        Args:
        - engine: Engine instance.
        - path (str): Path to the file to be managed. Defaults to "data/saves/save".
        """
        self.engine = engine
        self.path = path
        self.encryption_key = b"z8IwBgA-gFs66DrrM7JHtXe0fl9OVtL3A8Q-xU1nmAA="

    def set_encryption_key(self,encryption_key:bytes) -> None:
        """
        Set the encryption key for the SaveManager.

        Args:
        - encryption_key (bytes): New encryption key to be set.
        """
        self.encryption_key = encryption_key

    def generate_encryption_key(self) -> bytes:
        """
        Generate a new encryption key using Fernet.

        Returns:
        - bytes: Generated encryption key.
        """
        return Fernet.generate_key()
    
    def set_save_path(self,path:str) -> None:
        """
        Set the save path for the SaveManager.

        Args:
        - path (str): New path to be set for saving data.
        """
        self.path = path
    
    def __encrypt__(self,data:dict) -> bool:
        """
        !Used for internal functionality!
        Encrypt the provided data using Fernet encryption.

        Args:
        - data (dict): Data to be encrypted (as a dictionary).

        Returns:
        - bool: True if encryption is successful, False otherwise.
        """
        try:
            fernet = Fernet(self.encryption_key)
            encrypted_data = fernet.encrypt(bytes(json.dumps(data,ensure_ascii=True).encode("utf-8")))

            with open(self.path, 'wb') as file:
                file.write(encrypted_data)
        except Exception as e:
            self.engine.logger.error(e)
    
    def __decrypt__(self) -> bool|dict:
        """
        !Used for internal functionality!
        Decrypt the data in the file specified by the path using Fernet decryption.

        Returns:
        - bool | dict: Decrypted data as a dictionary if successful, False otherwise.
        """
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
        """
        Save data to the file using a specified key-value pair.

        Args:
        - key: Key for the data.
        - value: Value to be saved corresponding to the key.

        Returns:
        - bool: True if saving is successful, False otherwise.
        """
        try:
            data = self.__decrypt__()
            if data != False:
                data[key] = value
            else:
                data = {}
            self.__encrypt__(data)
            return True
        except Exception as e:
            self.engine.logger.error(e)

        return False
    
    def load(self,key) -> any:
        """
        Load data from the file using the specified key.

        Args:
        - key: Key to retrieve data.

        Returns:
        - any: Retrieved value corresponding to the key, or None if not found.
        """
        if os.path.exists(self.path):
            try:
                data = self.__decrypt__()
                if data != False:
                    return data[key]
            except Exception as e:
                self.engine.logger.error(e)
        else:
            return None
        
    def backup(self,backup_path:str="data/saves/backup"):
        """
        Create a backup of the current save file.

        Args:
        - backup_path (str): Path to store the backup file. Defaults to "data/saves/backup".
        """
        shutil.copyfile(
            self.path,
            os.path.join(backup_path,f'{os.path.split(self.path)[-1]}-{datetime.datetime.now().strftime("%H-%M-%S")}')
            )