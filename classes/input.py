import pygame
from classes.constances import *

class Input:
    def __init__(self,engine,joystick_dead_zone:int=0.15) -> None:
        
        self.engine = engine
        
        self.mouse = self.Mouse()

        self.keys = pygame.key.get_pressed()
        
        self.joystick_dead_zone = joystick_dead_zone
        self.joystick_devices = []

        for joystick in range(pygame.joystick.get_count()):
            self.joystick_devices.append(self.Joystick(pygame.joystick.Joystick(joystick)))
            
        self.registered_input = {
            "accept":[MOUSE_CLICK_LEFT,KEY_SPACE,KEY_RETURN,JOYSTICK_BUTTON_DOWN_CLICKED],
            "cancel":[KEY_ESCAPE,KEY_BACKSPACE,JOYSTICK_BUTTON_RIGHT_CLICKED],
            "right":[KEY_D,KEY_L,KEY_ARROW_RIGHT,JOYSTICK_DPAD_RIGHT_PRESSED,JOYSTICK_LEFT_STICK_HORIZONTAL],
            "left":[KEY_A,KEY_J,KEY_ARROW_LEFT,JOYSTICK_DPAD_LEFT_PRESSED,JOYSTICK_LEFT_STICK_HORIZONTAL],
            "up":[KEY_W,KEY_I,KEY_ARROW_UP,JOYSTICK_DPAD_UP_PRESSED,JOYSTICK_LEFT_STICK_VERTICAL],
            "down":[KEY_S,KEY_K,KEY_ARROW_DOWN,JOYSTICK_DPAD_DOWN_PRESSED,JOYSTICK_LEFT_STICK_VERTICAL],
            "screenshot":[KEY_P,KEY_F6]
        }

    def new(self,name:str,key:list[int,int]) -> bool:
        try:
            if name not in self.registered_input:
                self.registered_input[name] = []
            else:
                self.registered_input[name].append(key)
            return True
        except:
            return False
        
    def remove(self,inputname:str) -> bool:
        try:
            del self.registered_input[inputname]
            return True
        except:
            return False
        
    def get(self, name:str,controller_index:int=0) -> int|float:
        for key in self.registered_input[name]:
            if key[1] == KEYBOARD:
                if self.keys[key[0]]:
                    return 1
            elif key[1] == MOUSE:
                if self.mouse.get_button(key[0]):
                    return 1
            elif key[1] == JOYSTICK:
                if controller_index == -1:
                    for i in range(self.joystick_devices):
                        input_value = self.joystick_devices[controller_index].get_input(key)
                        if input_value != 0 and input_value != 0.0:
                            return input_value
                else:
                    if controller_index < len(self.joystick_devices)-1:
                        input_value = self.joystick_devices[controller_index].get_input(key)
                    else:
                        return 0
                if input_value != 0 and input_value != 0.0:
                    return input_value

        return 0
    
    def add_joystick(self,joystick:pygame.joystick.JoystickType) -> bool:
        try:
            self.joystick_devices.append(self.Joystick(pygame.joystick.Joystick(joystick)))
            return True
        except:
            return False
        
    def remove_joystick(self,controller_index:int) -> bool:
        try:
            self.joystick_devices.pop(controller_index)
            return True
        except:
            return False
        
    def update(self) -> None:
        self.keys = pygame.key.get_pressed()
        self.mouse.update()

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

        def update(self) -> None:
            self.left_clicked = False
            self.left_released = False
            self.middle_clicked = False
            self.middle_released = False
            self.right_clicked = False
            self.right_released = False
            self.position = [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]
            mouse_pressed = pygame.mouse.get_pressed()
            self.left_pressed = mouse_pressed[0]
            self.middle_pressed = mouse_pressed[1]
            self.right_pressed = mouse_pressed[2]

        def get_button(self,button:int) -> bool:
            mouse = [self.left_clicked,
                self.middle_clicked,
                self.right_clicked,
                self.left_pressed,
                self.middle_pressed,
                self.right_pressed,
                self.left_released,
                self.middle_released,
                self.right_released]
            return mouse[button]
        
        def get_pos(self) -> list[int,int]:
            return self.position

    class Joystick:
        def __init__(self,joystick:pygame.joystick.JoystickType) -> None:
            self.joystick = joystick
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
                0, # JOYSTICK_BUTTON_DOWN CLICKED
                0, # JOYSTICK_BUTTON_DOWN PRESSED
                0, # JOYSTICK_BUTTON_DOWN RELEASED
                0, # JOYSTICK_BUTTON_RIGHT CLICKED
                0, # JOYSTICK_BUTTON_RIGHT PRESSED
                0, # JOYSTICK_BUTTON_RIGHT RELEASED
                0, # JOYSTICK_BUTTON_UP CLICKED
                0, # JOYSTICK_BUTTON_UP PRESSED
                0, # JOYSTICK_BUTTON_UP RELEASED
                0, # JOYSTICK_BUTTON_LEFT CLICKED
                0, # JOYSTICK_BUTTON_LEFT PRESSED
                0, # JOYSTICK_BUTTON_LEFT RELEASED
                0, # JOYSTICK_DPAD_DOWN CLICKED
                0, # JOYSTICK_DPAD_DOWN PRESSED
                0, # JOYSTICK_DPAD_DOWN RELEASED
                0, # JOYSTICK_DPAD_RIGHT CLICKED
                0, # JOYSTICK_DPAD_RIGHT PRESSED
                0, # JOYSTICK_DPAD_RIGHT RELEASED
                0, # JOYSTICK_DPAD_UP CLICKED
                0, # JOYSTICK_DPAD_UP PRESSED
                0, # JOYSTICK_DPAD_UP RELEASED
                0, # JOYSTICK_DPAD_LEFT CLICKED
                0, # JOYSTICK_DPAD_LEFT PRESSED
                0, # JOYSTICK_DPAD_LEFT RELEASED
                0.0, # JOYSTICK_RIGHT_STICK_VERTICAL 
                0.0, # JOYSTICK_RIGHT_STICK_HORIZONTAL
                0, # JOYSTICK_RIGHT_STICK_CLICKED
                0, # JOYSTICK_RIGHT_STICK_PRESSED 
                0, # JOYSTICK_RIGHT_STICK_RELEASED
                0.0, # JOYSTICK_LEFT_STICK_VERTICAL 
                0.0, # JOYSTICK_LEFT_STICK_HORIZONTAL
                0, # JOYSTICK_LEFT_STICK_CLICKED
                0, # JOYSTICK_LEFT_STICK_PRESSED 
                0, # JOYSTICK_LEFT_STICK_RELEASED
                0, # JOYSTICK_BUTTON_SPEC_1 CLICKED
                0, # JOYSTICK_BUTTON_SPEC_1 PRESSED
                0, # JOYSTICK_BUTTON_SPEC_1 RELEASED
                0, # JOYSTICK_BUTTON_SPEC_2 CLICKED
                0, # JOYSTICK_BUTTON_SPEC_2 PRESSED
                0, # JOYSTICK_BUTTON_SPEC_2 RELEASED
                0, # JOYSTICK_RIGHT_BUMPER_CLICKED
                0, # JOYSTICK_RIGHT_BUMPER_PRESSED 
                0, # JOYSTICK_RIGHT_BUMPER_PRESSED 
                0, # JOYSTICK_LEFT_BUMPER_CLICKED
                0, # JOYSTICK_LEFT_BUMPER_PRESSED
                0, # JOYSTICK_LEFT_BUMPER_PRESSED
                0.0, # JOYSTICK_TRIGGER_R2
                0.0 # JOYSTICK_TRIGGER_L2
            ]
            joystick.init()

        def get_input(self,button:int) -> int|float:
            return self.inputs[button]
        
        def handle_input_event(self,event:pygame.Event) -> None:
            if event.type == pygame.JOYBUTTONDOWN:
                button_index = event.button
                self.inputs[JOYSTICK_BUTTON_MAP[self.type][button_index][0]] = True
                self.inputs[JOYSTICK_BUTTON_MAP[self.type][button_index][1]] = True
            
            elif event.type == pygame.JOYBUTTONUP:
                button_index = event.button
                self.inputs[JOYSTICK_BUTTON_MAP[self.type][button_index][1]] = False
                self.inputs[JOYSTICK_BUTTON_MAP[self.type][button_index][2]] = True

            elif event.type == pygame.JOYAXISMOTION:
                pass    # axis event

            elif event.type == pygame.JOYHATMOTION:
                print(event)    # Xbox dpad hat event