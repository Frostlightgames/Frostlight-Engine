import os
import json
import pygame
from classes.constances import *

class Input:
    def __init__(self,engine,joystick_dead_zone:int=0.15) -> None:
        
        # Engine variable
        self.engine = engine

        # Mouse variables        
        self.mouse = self.Mouse()
        self.reset_buttons = []

        # Keyboard variables
        self.keys = {}
        self.reset_keys = []
        
        # Joystick variables
        self.joystick_dead_zone = joystick_dead_zone
        self.joystick_devices = []
        
        # Input variables

        self.save_path = os.path.join("data","saves","input")

        self.registered_input = {
            "accept":[[MOUSE_LEFTCLICK,CLICKED],[KEY_SPACE,CLICKED],[KEY_RETURN,CLICKED],[JOYSTICK_BUTTON_DOWN,CLICKED]],
            "cancel":[[KEY_ESCAPE,CLICKED],[KEY_BACKSPACE,CLICKED],[JOYSTICK_BUTTON_RIGHT,CLICKED]],
            "right":[[KEY_D,PRESSED],[KEY_L,PRESSED],[KEY_ARROW_RIGHT,PRESSED],[JOYSTICK_DPAD_RIGHT,PRESSED],[JOYSTICK_LEFT_STICK_HORIZONTAL,PRESSED]],
            "left":[[KEY_A,PRESSED],[KEY_J,PRESSED],[KEY_ARROW_LEFT,PRESSED],[JOYSTICK_DPAD_LEFT,PRESSED],[JOYSTICK_LEFT_STICK_HORIZONTAL,PRESSED]],
            "up":[[KEY_W,PRESSED],[KEY_I,PRESSED],[KEY_ARROW_UP,PRESSED],[JOYSTICK_DPAD_UP,PRESSED],[JOYSTICK_LEFT_STICK_VERTICAL,PRESSED]],
            "down":[[KEY_S,PRESSED],[KEY_K,PRESSED],[KEY_ARROW_DOWN,PRESSED],[JOYSTICK_DPAD_DOWN,PRESSED],[JOYSTICK_LEFT_STICK_VERTICAL,PRESSED]],
            "screenshot":[[KEY_P,CLICKED],[KEY_F6,CLICKED]]
        }

        # Setting default value for keys
        for i in self.registered_input:
            for key in self.registered_input[i]:
                if key[0][1] == KEYBOARD:
                    self.keys[key[0][0]] = [False,False,False]

    def new(self,name:str,key:list[int,int],methode:int) -> bool:

        # Register/add new input
        try:
            if name not in self.registered_input:
                self.registered_input[name] = [[key,methode]]
            else:
                self.registered_input[name].append([key,methode])

            self.keys[key[0]] = [False,False,False]
            return True
        except:
            return False

        
    def remove(self,inputname:str) -> bool:

        # Remove registered input
        try:
            del self.registered_input[inputname]
            return True
        except:
            return False

    def reset(self,name:str,controller_index:int=-1):

        # Resets value of registered input to default
        for key in self.registered_input[name]:
            if key[0][1] == KEYBOARD:
                self.keys[key[0][0]] = [False,False,False]
                
            # Mouse values
            elif key[0][1] == MOUSE:
                self.mouse.buttons[key[0][0]] = [False,False,False]
                
            # Joystick values
            elif key[0][1] == JOYSTICK:
                if controller_index == -1:

                    # Resets value from all joysticks
                    for i in range(len(self.joystick_devices)):
                        self.joystick_devices[controller_index].inputs[key[0][0]] = [False,False,False]
                else:

                    # Resets value from specified joystick
                    if controller_index < len(self.joystick_devices):
                        self.joystick_devices[controller_index].inputs[key[0][0]] = [False,False,False]
                    else:
                        return 0
        
    def get(self, name:str,controller_index:int=-1) -> int|float:

        # Get input value from registered input
        for key in self.registered_input[name]:

            # Keyboard values
            if key[0][1] == KEYBOARD:
                if self.keys[key[0][0]][key[1]]:
                    return 1
                
            # Mouse values
            elif key[0][1] == MOUSE:
                print(self.mouse.buttons)
                if self.mouse.buttons[key[0][0]][key[1]]:
                    return 1
                
            # Joystick values
            elif key[0][1] == JOYSTICK:
                if controller_index == -1:

                    # Get value from not specified joystick
                    for i in range(len(self.joystick_devices)):
                        input_value = self.joystick_devices[i].get_input(key[0][0])
                        if input_value != 0 and input_value != 0.0:
                            return input_value
                else:

                    # Get value from specified joystick
                    if controller_index < len(self.joystick_devices):
                        input_value = self.joystick_devices[controller_index].get_input(key[0][0])
                    else:
                        return 0
                
                    # Filter joystick input value
                    if input_value != 0 or input_value != 0.0:
                        return input_value

        return 0
        
    def __update__(self) -> None:

        # Update all input devices
        for key in self.reset_keys:
            self.keys[key][0] = False
            self.keys[key][2] = False

        self.mouse.update()

        for joystick in self.joystick_devices:
            joystick.reset()

    def __handle_key_event__(self,event:pygame.Event):

        # Handel joystick button down event
        if event.type == pygame.KEYDOWN:
            self.keys[event.key] = [True,True,False]
            self.reset_keys.append(event.key)

        # Handel mouse button release event
        elif event.type == pygame.KEYUP:
            self.keys[event.key] = [False,False,True]
            self.reset_keys.append(event.key)

    def __handle_mouse_event__(self,event:pygame.Event):
        # Handel joystick button down event
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse.buttons[event.button-1] = [True,True,False]

        # Handel mouse button release event
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouse.buttons[event.button-1] = [False,False,True]

    def __handle_joy_event__(self,event:pygame.Event):

        # joystick specification
        joy_index = event.joy
        joy_type = self.joystick_devices[joy_index].type
        
        # Handel joystick button click event
        if event.type == pygame.JOYBUTTONDOWN:
            button_index = event.button
            self.joystick_devices[joy_index].inputs[JOYSTICK_BUTTON_MAP[joy_type][button_index][0][0]] = 1
            self.joystick_devices[joy_index].inputs[JOYSTICK_BUTTON_MAP[joy_type][button_index][1][0]] = 1

        # Handel joystick button release event
        elif event.type == pygame.JOYBUTTONUP:
            button_index = event.button
            self.joystick_devices[joy_index].inputs[JOYSTICK_BUTTON_MAP[joy_type][button_index][1][0]] = 0
            self.joystick_devices[joy_index].inputs[JOYSTICK_BUTTON_MAP[joy_type][button_index][2][0]] = 1

        # Handel joystick axis movement event
        elif event.type == pygame.JOYAXISMOTION:
            axis_index = event.axis
            value = 0.0

            # Detect deadzone
            if abs(event.value) > self.joystick_dead_zone:
                value = max(min(event.value,1.0),-1.0)
            self.joystick_devices[joy_index].inputs[JOYSTICK_AXIS_MAP[joy_type][axis_index][0]] = value

        elif event.type == pygame.JOYHATMOTION:

            # Xbox dpad hat event
            pass

    def __init_joysticks__(self) -> None:

        # Creates joystick device to be used
        self.joystick_devices = []
        for joystick in range(pygame.joystick.get_count()):
            self.joystick_devices.append(self.Joystick(pygame.joystick.Joystick(joystick)))

    def save(self):

        # Save registered input in file
        try:
            with open(self.save_path,"w+") as f:
                json.dump(self.registered_input,f)
            return True
        except:
            return False

    def load(self):

        # Load registered input in file
        try:
            with open(self.save_path,"r+") as f:
                self.registered_input = json.load(f)

                # Setting default value for keys
                for i in self.registered_input:
                    for key in self.registered_input[i]:
                        if key[0][1] == KEYBOARD:
                            self.keys[key[0][0]] = [False,False,False]
            return True
        except:
            return False

    class Mouse:
        def __init__(self) -> None:

            # Mouse variables
            self.position = [0,0]
            self.buttons = [
                [False,False,False],
                [False,False,False],
                [False,False,False]
            ]

        def update(self) -> None:

            # Reset mouse input values
            self.buttons[0][0] = False
            self.buttons[0][2] = False
            self.buttons[1][0] = False
            self.buttons[1][2] = False
            self.buttons[2][0] = False
            self.buttons[2][2] = False

            # Get mouse values
            self.position = [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]
            mouse_pressed = pygame.mouse.get_pressed()
            self.buttons[0][1] = mouse_pressed[0]
            self.buttons[1][1] = mouse_pressed[1]
            self.buttons[2][1] = mouse_pressed[2]

        def get_button(self,button:int) -> bool:

            # Get mouse button             
            return self.buttons[button]
        
        def get_pos(self) -> list[int,int]:

            # Getting mouse position
            return self.position

    class Joystick:
        def __init__(self,joystick:pygame.joystick.JoystickType) -> None:

            # Joystick variables
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
                0, # JOYSTICK_BUTTON_RIGHT CLICKED
                0, # JOYSTICK_BUTTON_UP CLICKED
                0, # JOYSTICK_BUTTON_LEFT CLICKED
                0, # JOYSTICK_DPAD_DOWN CLICKED
                0, # JOYSTICK_DPAD_RIGHT CLICKED
                0, # JOYSTICK_DPAD_UP CLICKED
                0, # JOYSTICK_DPAD_LEFT CLICKED
                0.0, # JOYSTICK_RIGHT_STICK_VERTICAL 
                0.0, # JOYSTICK_RIGHT_STICK_HORIZONTAL
                0, # JOYSTICK_RIGHT_STICK_CLICKED
                0.0, # JOYSTICK_LEFT_STICK_VERTICAL 
                0.0, # JOYSTICK_LEFT_STICK_HORIZONTAL
                0, # JOYSTICK_LEFT_STICK_CLICKED
                0, # JOYSTICK_BUTTON_SPEC_1 CLICKED
                0, # JOYSTICK_BUTTON_SPEC_2 CLICKED
                0, # JOYSTICK_RIGHT_BUMPER_CLICKED
                0, # JOYSTICK_LEFT_BUMPER_CLICKED
                0.0, # JOYSTICK_TRIGGER_R2
                0.0 # JOYSTICK_TRIGGER_L2
            ]

        def reset(self) -> None:

            # Reset joystick button click and releas values
            self.inputs[JOYSTICK_BUTTON_DOWN[0]] = 0
            self.inputs[JOYSTICK_BUTTON_RIGHT[0]] = 0
            self.inputs[JOYSTICK_BUTTON_UP[0]] = 0
            self.inputs[JOYSTICK_BUTTON_LEFT[0]] = 0
            self.inputs[JOYSTICK_DPAD_DOWN[0]] = 0
            self.inputs[JOYSTICK_DPAD_RIGHT[0]] = 0
            self.inputs[JOYSTICK_DPAD_UP[0]] = 0
            self.inputs[JOYSTICK_DPAD_LEFT[0]] = 0
            self.inputs[JOYSTICK_RIGHT_STICK[0]] = 0
            self.inputs[JOYSTICK_LEFT_STICK[0]] = 0
            self.inputs[JOYSTICK_BUTTON_SPECIAL_1[0]] = 0
            self.inputs[JOYSTICK_BUTTON_SPECIAL_2[0]] = 0
            self.inputs[JOYSTICK_RIGHT_BUMPER[0]] = 0
            self.inputs[JOYSTICK_LEFT_BUMPER[0]] = 0

        def get_input(self,button:int) -> int|float:

            # Get joystick button value
            return self.inputs[button]