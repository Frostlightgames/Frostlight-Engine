import os
import time
import pygame
import datetime

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
    GUI_ALIGN_CENTER = 0

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
        pygame.font.init()
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
        self.input = self._Input(self)
        self.gui = self._GUI(self)

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

        # Limits game fps
        self.clock.tick(self.fps)

        # Resets mouse click variables
        self.input._mouse_left_clicked = False
        self.input._mouse_left_released = False
        self.input._mouse_middle_clicked = False
        self.input._mouse_middle_released = False
        self.input._mouse_right_clicked = False
        self.input._mouse_right_released = False
        
        # Gets pygame Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            # Managing window events
            elif event.type == pygame.WINDOWMOVED:
                self.last_time = time.time()
                self.delta_time = 1

            elif event.type == pygame.VIDEORESIZE:
                if not self.fullscreen:
                    self.last_time = time.time()
                    self.delta_time = 1
                    self.changed_window_size = [event.w,event.h]
                    self.__manage_window_resize__()

            # Managing mouse events
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

        # Ends game loop
        self.run_game = False

    def get_fps(self):

        # Returns game fps as integer
        return int(min(self.clock.get_fps(),99999999))
    
    def create_file_structure():

        # Logging Variables
        directories_created = 0
        files_created = 0
        directories_to_create = ["data","screenshots",os.path.join("data","classes"),os.path.join("data","saves"),os.path.join("data","sprites")]

        # Creating logging file
        if not os.path.exists(os.path.join("data","log.txt")):
            files_created += 1

        # Creating directories
        for directory in directories_to_create:
            try:
                os.mkdir(directory)
                directories_created += 1
            except FileExistsError:
                Engine.log(f"Skipping creation of directory {directory}, it already exist.")

        # Creating main game file and write base game logic to it
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
        
        # Logging file creation
        if files_created == 0 and directories_created == 0:
            Engine.log("No new files and directories where created.")
        else:
            Engine.log(f"Created game files structure with {files_created} files and {directories_created} directories")

    def set_window_name(self,name:str):

        # Set the caption of the main window
        pygame.display.set_caption(name)

    def set_window_icon(self,path:list):

        # Setting the main windows icon
        pygame.display.set_icon(pygame.image.load(os.path.join(*path)).convert_alpha())

    def log(text:str):

        # Logs as Engine if log comes from engine file else as game
        with open(os.path.join("data","log.txt"),"+at") as file:
            if __name__ == "__main__":
                file.write(f"[Engine {datetime.datetime.now()}]: {text} \n")
            else:
                file.write(f"[Game {datetime.datetime.now()}]: {text} \n")
    
    def clear_log():

        # Clearing log by overwriting it
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

            # All mouse related variables
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

            self.mouse = [
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
            
            # All keyboard related variables
            self.keys = pygame.key.get_pressed()

            # Registered keyboard events
            self._registered_input = {
                "accept":[Engine.MOUSE_CLICK_LEFT,Engine.KEY_SPACE,Engine.KEY_RETURN],
                "cancel":[Engine.KEY_ESCAPE],
                "right":[Engine.KEY_D,Engine.KEY_ARROW_RIGHT],
                "left":[Engine.KEY_A,Engine.KEY_ARROW_LEFT],
                "up":[Engine.KEY_W,Engine.KEY_ARROW_UP],
                "down":[Engine.KEY_S,Engine.KEY_ARROW_DOWN]
            }

        def register_input(self,name:str,key:int):

            # Checks if input_name exists and adds input_link
            if name not in self._registered_input:
                self._registered_input[name] = []
            self._registered_input[name].append(key)

        def get_input(self, name:str):
            input_value = 0

            # Checking each option for an input
            for key in self._registered_input[name]:
                # Getting keyboard input value
                if key[1] == Engine.KEYBOARD:
                    if self.keys[key[0]]:
                        input_value = 1
                        break

                # Getting mouse input values
                elif key[1] == Engine.MOUSE:
                    if self.mouse[key[0]]:
                        input_value = 1
                        break
            
            # Return collected input value
            return input_value

        def _update(self):

            # Gets all mouse variables
            pygame_mouse_pressed = pygame.mouse.get_pressed()
            self._mouse_left_pressed = pygame_mouse_pressed[0]
            self._mouse_middle_pressed = pygame_mouse_pressed[1]
            self._mouse_right_pressed = pygame_mouse_pressed[2]
            
            self.mouse = [
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

            self.mouse_position = pygame.mouse.get_pos()

            # Gets all keyboard variables
            self.keys = pygame.key.get_pressed()
        
    class _GUI:
        def textrect(font,text:str) -> pygame.Rect:
            
            # Returns the  calculated rect size for a text
            rendered_text = font.render(text,True,(0,0,0))
            text_rect = rendered_text.get_rect()
            return text_rect
        
        class _GUI:
            def __init__(self,engine) -> None:
                self.engine = engine

        class Test(_GUI):
            def __init__(self, engine) -> None:
                super().__init__(engine)

            
            def render(self):
                pygame.draw.rect(self.engine.win,(255,255,255),pygame.Rect(64,64,64,64))

        class Text(_GUI):
            def render(text:str,
                       rect:pygame.Rect,
                       color:list[int,int,int]=[255,255,255],
                       font:pygame.font.Font=pygame.font.SysFont("Arial",18),
                       text_align=None,
                       surface:pygame.Surface=None):
                if type(font) == pygame.font.Font:
                    if text_align == None:
                        text_align = Engine.GUI_ALIGN_CENTER
                    if surface == None:
                        surface = Engine.win
                    text = font.render(text,True,color)
                    textrect = text.get_rect()
                    if text_align == 1:
                        textrect.center = (rect[2]//2+rect[0],rect[3]//2+rect[1])
                    elif text_align == 0:
                        h = rect[0]+5
                        textrect.center = (0,rect[3]//2+rect[1])
                        textrect.update(h,textrect[1],textrect[2],textrect[3])
                    surface.blit(text,textrect)
                else:
                    pass

        class Button(_GUI):
            def __init__(self,
                         surface:pygame.surface.Surface,
                         font,txt:str,pos:tuple[int,int],
                         size:tuple[int,int]=[0,0],
                         color_button:pygame.color.Color=(255,255,255),
                         color_hover:pygame.color.Color=(100,100,100),
                         color_text:pygame.color.Color=(0,0,0),
                         align_text:int=1,
                         border:int=0,
                         color_border:pygame.color.Color=(0,0,0),
                         border_radius:int=-1) -> None:
                self.win = surface
                self.font = font
                self.pos = pos
                self.size = size
                self.color_button = color_button
                self.color_hover = color_hover
                self.color_text = color_text
                self.align_text = align_text
                self.border = border
                self.color_border = color_border
                self.border_radius = border_radius
                self.clicked = False
                self.pressed = False
                self.text = txt
                self.txtrect = Engine.GUI.textrect(self.font,self.text)
                
                #button rect berechnen
                if self.size == 0 or (self.size[0] == 0 and self.size[1] == 0):
                    self.rect = pygame.Rect(self.pos[0],self.pos[1],(self.txtrect[2]/len(self.text))*(len(self.text)+2),self.txtrect[3]*1.2)
                elif self.size[0] == 0:  
                    self.rect = pygame.Rect(self.pos[0],self.pos[1],(self.txtrect[2]/len(self.text))*(len(self.text)+2),self.size[1])
                elif self.size[1] == 0:
                    self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.txtrect[3]*1.2)
                else:
                    self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                
                Engine.GUI.Text.render(self.text,self.rect,self.color_text,self.align_text)

            def draw(self):
                pygame.draw.rect(self.win,self.color_button,self.rect,0,self.border_radius)

                self.txt.draw(self.text,self.rect,self.color_text,self.align_text)
                if self.border > 0:
                    pygame.draw.rect(self.win,self.color_border,self.rect,self.border,self.border_radius)

            def update(self):
                self.mouse = [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]
                self.press = pygame.mouse.get_pressed()[0]
                self.click = pygame.mouse.get_pressed()[0]
                self.clicked = False
                if self.rect.collidepoint(self.mouse):
                    pygame.draw.rect(self.win,self.color_hover,self.rect)
                    if self.click:
                        self.clicked = True
                    
                self.txt.draw(self.text,self.rect,self.color_text,self.align_text)
                if self.border > 0:
                    pygame.draw.rect(self.win,self.color_border,self.rect,self.border,self.border_radius)    
        class DropDown:
            def __init__(self,surface:pygame.surface.Surface,font,txt:str,pos:tuple[int,int],size:tuple[int,int],color_button:pygame.color.Color=(255,255,255),color_hover:pygame.color.Color=(100,100,100),color_text:pygame.color.Color=(0,0,0),align_text='c',border=0,color_border:pygame.color.Color=(0,0,0),border_radius=-1,align_dropdown='l',dropdown_border=0,dropdown_border_color:pygame.color.Color=(0,0,0)) -> None:
                self.win = surface
                self.font = font
                self.pos = pos
                self.size = size
                self.txt = txt
                self.color_button = color_button
                self.color_hover = color_hover
                self.color_text = color_text
                self.align_text = align_text
                self.border = border
                self.border_radius = border_radius
                self.color_border = color_border
                self.align_dropdown = align_dropdown
                self.dropdown_border = dropdown_border
                self.dropdown_border_color = dropdown_border_color
                self.button = self.button(self.win,self.font,self.txt,self.pos,self.size,self.color_button,self.color_hover,self.color_text,self.align_text,self.border,self.color_border,self.border_radius)
                self.rect = self.button.rect
                self.objects = []
                self.active = False
                self.objects_activ = False

                if self.align_dropdown == 'rup':
                    self.y = self.button.rect[1]
                else:
                    self.y = self.button.rect[1]+self.button.rect[3]

            def load_objects(self):
                pass

            def add_object(self,text:str,dropdown:bool=False,color_button:pygame.color.Color=None,color_hover:pygame.color.Color=None,color_text:pygame.color.Color=None,color_border:pygame.color.Color=None,text_align='l',border=0,font=None,border_radius=-1,align_dropdown='l',dropdown_border=0,dropdown_border_color:pygame.color.Color=(0,0,0)):
                
                #berechnung für neues object
                #append

                
                if font == None:
                    font = self.font     
                if color_button == None:
                    color_button = self.color_button    
                if color_hover == None:
                    color_hover = self.color_hover
                if color_text == None:
                    color_text = self.color_text
                if color_border == None:
                    color_border = self.color_border

                if len(self.objects) == 0:
                    x = self.textrect(font,text)[2]*1.1
                else:
                    x = self.bigges_text_rect(self.objects,font,text)[2]*1.1

                if dropdown:
                    if self.align_dropdown.startswith('r'):
                        self.objects.append(self.DropDown(self.win,font,text,(self.button.rect[0]+self.button.rect[2],self.y),(x,0),color_button,color_hover,color_text,text_align,border,color_border,align_dropdown='rup'))
                    else:
                        self.objects.append(self.DropDown(self.win,font,text,(self.button.rect[0],self.y),(x,0),color_button,color_hover,color_text,text_align,border,color_border))
                else:
                    if self.align_dropdown.startswith('r'):
                        self.objects.append(self.Button(self.win,font,text,(self.button.rect[0]+self.button.rect[2],self.y),(x,0),color_button,color_hover,color_text,text_align,border,color_border))
                    else:
                        self.objects.append(self.Button(self.win,font,text,(self.button.rect[0],self.y),(x,0),color_button,color_hover,color_text,text_align,border,color_border))
                
                self.y += self.objects[len(self.objects)-1].rect[3]

                x = 0
                for o in self.objects:
                    o.rect[2] = self.bigges_text_rect(self.objects,font)[2]*1.1
                    x += o.rect[3]
                self.DropDown_rect = pygame.Rect(self.objects[0].rect[0],self.objects[0].rect[1],self.objects[len(self.objects)-1].rect[2],x)

            def draw_dropdown(self):
                for btn in self.objects:
                    btn.draw()
            
            def bigges_text_rect(self,text,font,new_object:str='') -> pygame.Rect:

                # Retunes the biggest text rect in a list
                x = 0
                for i in range(len(text)):
                    a = len(text[i])
                    b = len(text[x])
                    if a > b:
                        x = i

                if type(text[x]) == self.Button:
                    if len(text[x].text) > len(new_object):
                        t = self.textrect(font,text[x].text)
                    else:
                        t = self.textrect(font,new_object)
                elif type(text[x]) == self.DropDown:
                    if len(text[x].Button.text) > len(new_object):
                        t = self.textrect(font,text[x].Button.text)
                    else:
                        t = self.textrect(font,new_object)
                else:
                    if len(text[x]) > len(new_object):
                        t = self.textrect(font,text[x])
                    else:
                        t = self.textrect(font,new_object)
                return t
        
            def draw(self):
                self.button.draw()

            def update(self):
                self.mouse = [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]
                self.click = pygame.mouse.get_pressed()[0]
                self.button.update()
                if self.button.clicked:
                    self.active = True
                if self.active or self.objects_activ:
                    for object in self.objects:
                        if type(object) == self.DropDown:
                            if object.active:
                                self.objects_activ = True
                            
                    boolean = self.DropDown_rect.collidepoint(self.mouse) == False and self.click
                    if boolean:
                        self.active = False
                        pygame.draw.rect(self.win,(255,0,255),self.DropDown_rect,1)
                    self.draw_dropdown()
                    for btn in self.objects:
                        btn.update()

                    if self.dropdown_border > 0:
                        pygame.draw.rect(self.win,self.dropdown_border_color,self.DropDown_rect,self.dropdown_border)
if __name__ == "__main__":
    Engine.create_file_structure()