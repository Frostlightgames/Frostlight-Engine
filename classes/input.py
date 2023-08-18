import pygame
from classes.constances import *

class Input:
    def __init__(self,engine,joystick_dead_zone:int=0.15) -> None:
        
        self.engine = engine
        
        self.mouse = self.Mouse()

        self.joystick_dead_zone = joystick_dead_zone
        self.joystick_devices = []
        
        for joystick in range(pygame.joystick.get_count()):
            self.joystick_devices.append(self.Joystick(pygame.joystick.Joystick(joystick)))
            
        self.registered_input = {
            "accept":[MOUSE_CLICK_LEFT,KEY_SPACE,KEY_RETURN,JOYSTICK_BUTTON_DOWN],
            "cancel":[KEY_ESCAPE,KEY_BACKSPACE,JOYSTICK_BUTTON_RIGHT],
            "right":[KEY_D,KEY_L,KEY_ARROW_RIGHT,JOYSTICK_DPAD_RIGHT,JOYSTICK_LEFT_STICK_RIGHT],
            "left":[KEY_A,KEY_J,KEY_ARROW_LEFT,JOYSTICK_DPAD_LEFT,JOYSTICK_LEFT_STICK_LEFT],
            "up":[KEY_W,KEY_I,KEY_ARROW_UP,JOYSTICK_DPAD_UP,JOYSTICK_LEFT_STICK_UP],
            "down":[KEY_S,KEY_K,KEY_ARROW_DOWN,JOYSTICK_DPAD_DOWN,JOYSTICK_LEFT_STICK_DOWN],
            "screenshot":[KEY_P,KEY_F6]
        }

    def new(self,name:str,key:list[int,int],joystick_device_index:int=-1):
        if name not in self.registered_input:
            self.registered_input[name] = []
        if key[1] == JOYSTICK:
            self.registered_input[name].append([key[0],key[1],joystick_device_index])
        else:
            self.registered_input[name].append(key)

    def remove(self,inputname:str):
        del self.registered_input[inputname]

    def get(self, name:str):
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
            if key[1] == KEYBOARD:
                if keys[key[0]]:
                    key_pressed = 1
                    break
            elif key[1] == MOUSE:
                if mouse[key[0]]:
                    key_pressed = 1
                    break
            elif key[1] == JOYSTICK:
                if self._joystick[key[0]] != 0:
                    key_pressed = 1
                    break
        
        return key_pressed
    
    def add_joystick(self,joystick:pygame.joystick.JoystickType):
        self.joystick_devices.append(self.Joystick(pygame.joystick.Joystick(joystick)))

    def remove_joystick(self,device_id:int):
        self.joystick_devices.pop(device_id)

    def update(self,engine):
        pygame_mouse_pressed = pygame.mouse.get_pressed()
        self._mouse_left_pressed = pygame_mouse_pressed[0]
        self._mouse_middle_pressed = pygame_mouse_pressed[1]
        self._mouse_right_pressed = pygame_mouse_pressed[2]

        self.mouse_position = list(pygame.mouse.get_pos())
        if self.last_mouse_position != self.mouse_position:
            self.mouse = self.mouse_position
        self.last_mouse_position = self.mouse_position

        for joystick in self.joystick_devices:
            value = joystick.get_axis(0)
            if abs(value) > 0.15:
                self.mouse[0] += value*1000*engine.delta_time
            value = joystick.get_axis(1)
            if abs(value) > 0.15:
                self.mouse[1] += value*1000*engine.delta_time
            value = joystick.get_axis(2)
            if abs(value) > 0.15:
                self.mouse[0] += value*1000*engine.delta_time
            value = joystick.get_axis(3)
            if abs(value) > 0.15:
                self.mouse[1] += value*1000*engine.delta_time

    class Mouse:
        def __init__(self) -> None:
            self.position = [0,0]
            self.left_pressed = False
            self.left_clicked = False
            self.left_released = False
            self.middle_pressed = False
            self.middle_clicked = False
            self.middle_released = False
            self.right_pressed = False
            self.right_clicked = False
            self.right_released = False

        def update(self):
            self.position = [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]
            mouse_pressed = pygame.mouse.get_pressed()
            self.left_pressed = mouse_pressed[0]
            self.middle_pressed = mouse_pressed[1]
            self.right_pressed = mouse_pressed[2]

    class Joystick:
        def __init__(self,joystick:pygame.joystick.JoystickType) -> None:
            self.name = joystick.get_name()
            if self.name == "Xbox 360 Controller":
                self.type = XBOX_360_CONTROLLER
            elif self.name == "PS4 Controller":
                self.type = PLAYSTATION_4_CONTROLLER
            elif self.name == "Sony Interactive Entertainment Wireless Controller":
                self.type = PLAYSTATION_5_CONTROLLER
            elif self.name == "Nintendo Switch Pro Controller":
                self.type = NINTENDO_SWITCH_PRO_CONTROLLER
            elif self.name == "Nintendo Switch Joy-Con (L)":
                self.type = NINTENDO_SWITCH_JOYCON_CONTROLLER_L
            elif self.name == "Nintendo Switch Joy-Con (R)":
                self.type = NINTENDO_SWITCH_JOYCON_CONTROLLER_R
            elif self.name == "Nintendo Switch Joy-Con (L/R)":
                self.type = NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R
            else:
                self.type = XBOX_360_CONTROLLER
            self.battery = joystick.get_power_level()
            self.device_id = joystick.get_id()
            self.instance_id = joystick.get_instance_id()
            self.guid = joystick.get_guid()
            self.inputs = [
                [0,0,0], # JOYSTICK_BUTTON_DOWN
                [0,0,0], # JOYSTICK_BUTTON_RIGHT
                [0,0,0], # JOYSTICK_BUTTON_UP
                [0,0,0], # JOYSTICK_BUTTON_LEFT
                [0,0,0], # JOYSTICK_DPAD_DOWN
                [0,0,0], # JOYSTICK_DPAD_RIGHT
                [0,0,0], # JOYSTICK_DPAD_UP
                [0,0,0], # JOYSTICK_DPAD_LEFT
                [0,0,0], # JOYSTICK_BUTTON_SPEC_1 
                [0,0,0], # JOYSTICK_BUTTON_SPEC_2
                0.0, # JOYSTICK_RIGHT_STICK_DOWN 
                0.0, # JOYSTICK_RIGHT_STICK_RIGHT
                0.0, # JOYSTICK_RIGHT_STICK_UP
                0.0, # JOYSTICK_RIGHT_STICK_LEFT 
                0.0, # JOYSTICK_LEFT_STICK_DOWN
                0.0, # JOYSTICK_LEFT_STICK_RIGHT 
                0.0, # JOYSTICK_LEFT_STICK_UP
                0.0, # JOYSTICK_LEFT_STICK_LEFT
                0.0, # JOYSTICK_TRIGGER_R1
                0.0, # JOYSTICK_TRIGGER_L1
                0.0, # JOYSTICK_TRIGGER_R2
                0.0 # JOYSTICK_TRIGGER_L2
            ]