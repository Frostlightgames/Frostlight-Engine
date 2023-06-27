import os
import time
import socket
import pygame
import datetime
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad,unpad

class Engine:
    
    # Custom variables go here
    KEYBOARD = 0
    MOUSE = 1
    JOYSTICK = 2
    
    KEY_A = [pygame.K_a,KEYBOARD]
    KEY_B = [pygame.K_b,KEYBOARD]
    KEY_C = [pygame.K_c,KEYBOARD]
    KEY_D = [pygame.K_d,KEYBOARD]
    KEY_E = [pygame.K_e,KEYBOARD]
    KEY_F = [pygame.K_f,KEYBOARD]
    KEY_G = [pygame.K_g,KEYBOARD]
    KEY_H = [pygame.K_h,KEYBOARD]
    KEY_I = [pygame.K_i,KEYBOARD]
    KEY_J = [pygame.K_j,KEYBOARD]
    KEY_K = [pygame.K_k,KEYBOARD]
    KEY_L = [pygame.K_l,KEYBOARD]
    KEY_M = [pygame.K_m,KEYBOARD]
    KEY_N = [pygame.K_n,KEYBOARD]
    KEY_O = [pygame.K_o,KEYBOARD]
    KEY_P = [pygame.K_p,KEYBOARD]
    KEY_Q = [pygame.K_q,KEYBOARD]
    KEY_R = [pygame.K_r,KEYBOARD]
    KEY_S = [pygame.K_s,KEYBOARD]
    KEY_T = [pygame.K_t,KEYBOARD]
    KEY_U = [pygame.K_u,KEYBOARD]
    KEY_V = [pygame.K_v,KEYBOARD]
    KEY_W = [pygame.K_w,KEYBOARD]
    KEY_X = [pygame.K_x,KEYBOARD]
    KEY_Y = [pygame.K_y,KEYBOARD]
    KEY_Z = [pygame.K_z,KEYBOARD]
    KEY_ARROW_LEFT = [pygame.K_LEFT,KEYBOARD]
    KEY_ARROW_RIGHT = [pygame.K_RIGHT,KEYBOARD]
    KEY_ARROW_UP = [pygame.K_UP,KEYBOARD]
    KEY_ARROW_DOWN = [pygame.K_DOWN,KEYBOARD]
    KEY_RETURN = [pygame.K_RETURN,KEYBOARD]
    KEY_SPACE = [pygame.K_SPACE,KEYBOARD]
    KEY_ESCAPE = [pygame.K_ESCAPE,KEYBOARD]
    MOUSE_CLICK_LEFT = [0,MOUSE]
    MOUSE_CLICK_MIDDLE = [1,MOUSE]
    MOUSE_CLICK_RIGHT = [2,MOUSE]
    MOUSE_PRESSED_LEFT = [3,MOUSE]
    MOUSE_PRESSED_MIDDLE = [4,MOUSE]
    MOUSE_PRESSED_RIGHT = [5,MOUSE]
    MOUSE_UP_LEFT = [6,MOUSE]
    MOUSE_UP_MIDDLE = [7,MOUSE]
    MOUSE_UP_RIGHT = [8,MOUSE]

    def __init__(self,
                 fps:int=0,
                 fullscreen:bool=False,
                 game_version:str="1.0",
                 language:str="en",
                 mouse_visible:bool=True,
                 nowindow:bool=False,
                 resizable:bool=True,
                 sounds:bool=True,
                 vsync:bool=False,
                 window_centered:bool=True,
                 window_depth:int=1,
                 window_name:str="New Game",
                 window_size:list=[1920,1080]):
        
        # initialize all modules
        pygame.init()
        pygame.joystick.init()
        if sounds:
            pygame.mixer.pre_init(44100,-16,2,512)

        # Boolean variables go here
        self.fullscreen = fullscreen
        self.mouse_visible = mouse_visible
        self.nowindow = nowindow
        self.resizable = resizable
        self.run_game = True
        self.sounds = sounds
        self.vsync = vsync
        self.window_centered = window_centered

        # Integer and float variables go here
        self.fps = fps
        self.delta_time = 1
        self.last_time = time.time()
        self.version = 0.1
        self.window_depth = window_depth

        # String variables go here
        self.game_state = "intro"
        self.game_version = game_version
        self.language = language
        self.window_name = window_name

        # List variables go here
        self.window_size = window_size
        self.changed_window_size = self.window_size

        # Class variables go here
        self.input = self._Input()

        self.__create_window__()

    def __create_window__(self):
        if not self.nowindow:
            pygame.display.init()
            
            # Center window
            if self.window_centered:
                os.environ['SDL_VIDEO_CENTERED'] = '1'
            else:
                os.environ['SDL_VIDEO_CENTERED'] = '0'

            # Create window
            create_window_size = [int(pygame.display.Info().current_w),int(pygame.display.Info().current_h)]
            if self.fullscreen: # Fullscreen window
                self.win = pygame.display.set_mode(create_window_size,pygame.FULLSCREEN,vsync=self.vsync,depth=self.window_depth)
            else:

                # Calculate fitting window size
                if self.window_size != [1920,1080]:
                    create_window_size = self.window_size
                else:
                    create_window_size = [create_window_size[0],create_window_size[1]*0.94]

                if self.resizable: # Resizable window
                    self.win = pygame.display.set_mode(create_window_size,pygame.RESIZABLE,vsync=self.vsync,depth=self.window_depth)
                else: # Fixed size window
                    self.win = pygame.display.set_mode(create_window_size,vsync=self.vsync,depth=self.window_depth)
            
            # Set window variables
            self.clock = pygame.time.Clock()
            self.window_size = [int(pygame.display.Info().current_w),int(pygame.display.Info().current_h)]
            
            # Change window attributes
            pygame.display.set_caption(self.window_name)
            pygame.mouse.set_visible(self.mouse_visible)

    def __get_events__(self):

        self.clock.tick(self.fps)

        self.input._mouse_left_clicked = False
        self.input._mouse_left_released = False
        self.input._mouse_middle_clicked = False
        self.input._mouse_middle_released = False
        self.input._mouse_right_clicked = False
        self.input._mouse_right_released = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            # Window events
            elif event.type == pygame.WINDOWMOVED:
                self.last_time = time.time()
                self.delta_time = 1

            elif event.type == pygame.VIDEORESIZE:
                if not self.fullscreen:
                    self.last_time = time.time()
                    self.delta_time = 1
                    self.changed_window_size = [event.w,event.h]
                    self.__manage_window_resize__()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.input._mouse_left_released = True
                if event.button == 2:
                    self.input._mouse_middle_released = True
                if event.button == 3:
                    self.input._mouse_right_released = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.input._mouse_left_clicked = True
                if event.button == 2:
                    self.input._mouse_middle_clicked = True
                if event.button == 3:
                    self.input._mouse_right_clicked = True
    
    def __manage_window_resize__(self):
        if self.resizable: # Resizable window
            self.win = pygame.display.set_mode(self.changed_window_size,pygame.RESIZABLE,vsync=self.vsync,depth=self.window_depth)
        else: # Fixed size window
            self.win = pygame.display.set_mode(self.changed_window_size,vsync=self.vsync,depth=self.window_depth)

    def update(self):
        self.input._update()
        self.delta_time = time.time()-self.last_time
        self.last_time = time.time()

    def draw(self):
        pass

    def run(self):
        Engine.log("Starting game")
        while self.run_game:
            self.__get_events__()
            self.update()
            self.draw()

    def quit(self):
        self.run_game = False

    def get_fps(self):
        return int(min(self.clock.get_fps(),99999999))
    
    def create_file_structure():
        directories_created = 0
        files_created = 0
        directories_to_create = ["data","screenshots",os.path.join("data","classes"),os.path.join("data","saves"),os.path.join("data","sprites")]

        if not os.path.exists(os.path.join("data","log.txt")):
            files_created += 1

        for directory in directories_to_create:
            try:
                os.mkdir(directory)
                directories_created += 1
            except FileExistsError:
                Engine.log(f"Skipping creation of directory {directory}, it already exist.")

        if not os.path.exists("main.py"):
            with open("main.py","+wt") as file:
                file.write("from frostlight_engine import Engine\n")
                file.write("\n")
                file.write("class Game(Engine):\n")
                file.write("    def __init__(self):\n")
                file.write("        super().__init__()\n")
                file.write("\n")
                file.write("    def update(self):\n")
                file.write("        super().update()\n")
                file.write("\n")
                file.write('        if self.game_state == "intro":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "menu":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "game":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "credits":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write("    def draw(self):\n")
                file.write("        super().draw()\n")
                file.write("\n")
                file.write('        if self.game_state == "intro":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "menu":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "game":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "credits":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('if __name__ == "__main__":\n')
                file.write("    game = Game()\n")
                file.write("    game.run()\n")
            files_created += 1
        else:
            Engine.log("Skipping creation of main file, already exist.")

        if files_created == 0 and directories_created == 0:
            Engine.log("No new files and directories where created.")
        else:
            Engine.log(f"Created game files structure with {files_created} files and {directories_created} directories")

    def set_window_name(self,name:str):
        pygame.display.set_caption(name)

    def set_window_icon(self,path:list):
        pygame.display.set_icon(pygame.image.load(os.path.join(*path)).convert_alpha())

    def log(text:str):
        with open(os.path.join("data","log.txt"),"+at") as file:
            if __name__ == "__main__":
                file.write(f"[Engine {datetime.datetime.now()}]: {text} \n")
            else:
                file.write(f"[Game {datetime.datetime.now()}]: {text} \n")
    
    def clear_log():
        with open(os.path.join("data","log.txt"),"w") as file:
            file.write("")

    def scale_rect(rect, amount) -> pygame.Rect:
        c = rect.center
        w = rect.width * amount
        h = rect.height * amount
        new = pygame.Rect(0,0,w,h)
        new.center = c
        return new

    class _Input:
        def __init__(self) -> None:
            self.mouse_position = [0,0]
            self._mouse_left_pressed = False
            self._mouse_left_clicked = False
            self._mouse_left_released = False
            self._mouse_middle_pressed = False
            self._mouse_middle_clicked = False
            self._mouse_middle_released = False
            self._mouse_right_pressed = False
            self._mouse_right_clicked = False
            self._mouse_right_released = False
            
            self._registered_input = {
                "accept":[Engine.MOUSE_CLICK_LEFT,Engine.KEY_SPACE,Engine.KEY_RETURN],
                "cancel":[Engine.KEY_ESCAPE],
                "right":[Engine.KEY_D,Engine.KEY_ARROW_RIGHT],
                "left":[Engine.KEY_A,Engine.KEY_ARROW_LEFT],
                "up":[Engine.KEY_W,Engine.KEY_ARROW_UP],
                "down":[Engine.KEY_S,Engine.KEY_ARROW_DOWN]
            }

        def register_input(self,name:str,key:int):
            if name not in self._registered_input:
                self._registered_input[name] = []
            self._registered_input[name].append(key)

        def get_input(self, name:str):
            keys = pygame.key.get_pressed()
            mouse = [
                self._mouse_left_clicked,
                self._mouse_middle_clicked,
                self._mouse_right_clicked,
                self._mouse_left_pressed,
                self._mouse_middle_pressed,
                self._mouse_right_pressed,
                self._mouse_left_released,
                self._mouse_middle_released,
                self._mouse_right_released,
                ]
            
            key_pressed = 0
            for key in self._registered_input[name]:
                if key[1] == Engine.KEYBOARD:
                    if keys[key[0]]:
                        key_pressed = 1
                        break
                elif key[1] == Engine.MOUSE:
                    if mouse[key[0]]:
                        key_pressed = 1
                        break
            
            return key_pressed

        def _update(self):
            pygame_mouse_pressed = pygame.mouse.get_pressed()
            self._mouse_left_pressed = pygame_mouse_pressed[0]
            self._mouse_middle_pressed = pygame_mouse_pressed[1]
            self._mouse_right_pressed = pygame_mouse_pressed[2]

            self.mouse_position = pygame.mouse.get_pos()

    class _Console:
        class Colors:
            HEADER = '\033[95m'
            BLUE = '\033[94m'
            CYAN = '\033[96m'
            GREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'

    class _Network:

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
                                package = Engine._Network.Package.pack([0x01],"i")
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
                            package = package = Engine._Network.Package.pack([0x02],"i")
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
                            package += Engine._Network.Package.pack([ord(letter)],"i")
                        result += Engine._Network.Package.pack([len(chunk)],"i")
                
                return result

if __name__ == "__main__":
    Engine.create_file_structure()