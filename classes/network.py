import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad,unpad

class Network:
    def generate_keypair(bytes:int):
        key = RSA.generate(bytes)
        private_key = key.export_key('PEM')
        return key, private_key
    
    class Client:
        def __init__(self,conn:socket.socket,rsakey:RSA.RsaKey,protocol_version:int):
            self.socket = conn
            self.aeskey = ""
            self.aesiv = ""
            self.rsakey = rsakey
            self.private_key = self.rsakey.export_key('PEM')
            self.protocol_version = protocol_version
            self.connected = False
            self.package_lost = 0

        def encrypt(self,data,key,iv) -> bytes:
            cipher = AES.new(key,AES.MODE_CBC,iv)
            return cipher.encrypt(pad(data,AES.block_size))

        def decrypt(self,data,key,iv) -> bytes:
            cipher = AES.new(key,AES.MODE_CBC,iv)
            return unpad(cipher.decrypt(data),AES.block_size)

        def send(self,data:bytes):
            try:
                data = self.encrypt(data,self.aeskey,self.aesiv)
                self.socket.send(data)
            except Exception:
                self.package_lost += 1

        def recv(self,buffer:int) -> list:
            try:
                encrypted_data = self.socket.recv(buffer)
                if encrypted_data:
                    data = self.decrypt(encrypted_data,self.aeskey,self.aesiv)
                    package_id = int.from_bytes(data[:1],"big")
                    return [package_id,data[1:]]
            except Exception:
                self.package_lost += 1
                return [None,None]
        
        def recv_raw(self,buffer:int) -> bytes:
            try:
                data = self.socket.recv(buffer)
                if data:
                    return data
            except Exception:
                self.package_lost += 1

        def send_raw(self,data:bytes):
            try:
                self.socket.send(data)
            except Exception:
                self.package_lost += 1

        def authenticate_client(self) -> bool:
            try:
                data = self.socket.recv(8)
                if int.from_bytes(data[:1],"big") == 0x00:
                    if int.from_bytes(data[1:2],"big") == self.protocol_version:
                        package = 0x00.to_bytes(1,"big")+self.rsakey.export_key("DER")
                        self.socket.send(package)
                        encrypted_data = self.socket.recv(1024)
                        private_key = RSA.importKey(self.private_key)
                        private_key = PKCS1_OAEP.new(private_key)
                        data = private_key.decrypt(encrypted_data)
                        if int.from_bytes(data[:1],"big") == 0x01:
                            self.aeskey = data[1:17]
                            self.aesiv = data[17:]
                            package = Network.Package.pack([0x01],"i")
                            self.send(package)
                            package_id,data = self.recv(16)
                            if package_id == 0x02:
                                self.connected = True
                                return True
                self.send_raw(bytes(0xF0))
                return False
            except Exception:
                return False
            
    class Server:
        def __init__(self,conn:socket.socket,aeskey,aesiv,protocol_version:int):
            self.socket = conn
            self.aeskey = aeskey
            self.aesiv = aesiv
            self.protocol_version = protocol_version
            self.connected = False
            self.package_lost = 0

        def encrypt(self,data,key,iv) -> bytes:
            cipher = AES.new(key,AES.MODE_CBC,iv)
            return cipher.encrypt(pad(data,AES.block_size))

        def decrypt(self,data,key,iv) -> bytes:
            cipher = AES.new(key,AES.MODE_CBC,iv)
            return unpad(cipher.decrypt(data),AES.block_size)

        def send(self,data:bytes):
            try:
                data = self.encrypt(data,self.aeskey,self.aesiv)
                self.socket.send(data)
            except Exception as e:
                self.package_lost += 1

        def recv(self,buffer:int) -> list:
            try:
                encrypted_data = self.socket.recv(buffer)
                if encrypted_data:
                    data = self.decrypt(encrypted_data,self.aeskey,self.aesiv)
                    package_id = int.from_bytes(data[:1],"big")
                    return [package_id,data[1:]]
            except Exception:
                self.package_lost += 1
                return [None,None]

        def recv_raw(self,buffer:int) -> bytes:
            try:
                data = self.socket.recv(buffer)
                if data:
                    return data
            except Exception as e:
                self.package_lost += 1

        def send_raw(self,data:bytes):
            try:
                self.socket.send(data)
            except Exception as e:
                self.package_lost += 1
        
        def auth_with_server(self) -> bool:
            try:
                package = 0x00.to_bytes(1,"big")+self.protocol_version.to_bytes(1,"big")
                self.socket.send(package)
                data = self.socket.recv(1024)
                if int.from_bytes(data[:1],"big") == 0x00:
                    importkey = RSA.importKey(data[1:])
                    publickey = PKCS1_OAEP.new(importkey)
                    package = publickey.encrypt(0x01.to_bytes(1,"big")+self.aeskey+self.aesiv)
                    self.socket.send(package)
                    package_id,data = self.recv(16)
                    if package_id == 0x01:
                        package = package = Network.Package.pack([0x02],"i")
                        self.send(package)
                        self.connected = True
                        return True
                return False
            except Exception:
                return False
    
    class Package:
        def unpack(sequence:str,data:bytes) -> list:
            result = []
            for datatype in sequence:
                if datatype == "b":
                    if data[:1] == b"\x00":
                        result.append(False)
                    else:
                        result.append(True)
                    data = data[1:]
                elif datatype == "i":
                    result.append(int.from_bytes(data[:1],"big"))
                    data = data[1:]
                elif datatype == "p":
                    result.append(int.from_bytes(data[:2],"big"))
                    data = data[2:]
                elif datatype == "s":
                    length = int.from_bytes(data[:1],"big")
                    data = data[1:]
                    result.append(data[:length].decode("utf-8"))
                    data = data[length:]
            if data:
                result.append(data)
            return result
        
        def pack(data:list,sequence:str) -> bytes:
            result = b""
            for i,chunk in enumerate(data):
                if sequence[i] == "b":
                    if chunk:
                        result += bytes(1).fromhex("01")
                    result += bytes(1).fromhex("00")
                
                if sequence[i] == "i":
                    if chunk > 255 or chunk < 0:
                        raise OverflowError
                    result += chunk.to_bytes(1,"big")

                if sequence[i] == "p":
                    if chunk > 65535 or chunk < 0:
                        raise OverflowError
                    result += chunk.to_bytes(2,"big")

                if sequence[i] == "s":
                    if len(chunk) > 255:
                        raise OverflowError
                    package = b""
                    for letter in chunk:
                        package += Network.Package.pack([ord(letter)],"i")
                    result += Network.Package.pack([len(chunk)],"i")
            
            return result