import os
import json
import math
import pygame

# Input types
_KEYBOARD = 0
_MOUSE = 1
_JOYSTICK = 2

# Input method
CLICKED = 0
PRESSED = 1
RELEASE = 2

# Keyboard input index
KEY_A = [pygame.K_a,_KEYBOARD]
KEY_B = [pygame.K_b,_KEYBOARD]
KEY_C = [pygame.K_c,_KEYBOARD]
KEY_D = [pygame.K_d,_KEYBOARD]
KEY_E = [pygame.K_e,_KEYBOARD]
KEY_F = [pygame.K_f,_KEYBOARD]
KEY_G = [pygame.K_g,_KEYBOARD]
KEY_H = [pygame.K_h,_KEYBOARD]
KEY_I = [pygame.K_i,_KEYBOARD]
KEY_J = [pygame.K_j,_KEYBOARD]
KEY_K = [pygame.K_k,_KEYBOARD]
KEY_L = [pygame.K_l,_KEYBOARD]
KEY_M = [pygame.K_m,_KEYBOARD]
KEY_N = [pygame.K_n,_KEYBOARD]
KEY_O = [pygame.K_o,_KEYBOARD]
KEY_P = [pygame.K_p,_KEYBOARD]
KEY_Q = [pygame.K_q,_KEYBOARD]
KEY_R = [pygame.K_r,_KEYBOARD]
KEY_S = [pygame.K_s,_KEYBOARD]
KEY_T = [pygame.K_t,_KEYBOARD]
KEY_U = [pygame.K_u,_KEYBOARD]
KEY_V = [pygame.K_v,_KEYBOARD]
KEY_W = [pygame.K_w,_KEYBOARD]
KEY_X = [pygame.K_x,_KEYBOARD]
KEY_Y = [pygame.K_y,_KEYBOARD]
KEY_Z = [pygame.K_z,_KEYBOARD]
KEY_F1 = [pygame.K_F1,_KEYBOARD]
KEY_F2 = [pygame.K_F2,_KEYBOARD]
KEY_F3 = [pygame.K_F3,_KEYBOARD]
KEY_F4 = [pygame.K_F4,_KEYBOARD]
KEY_F5 = [pygame.K_F5,_KEYBOARD]
KEY_F6 = [pygame.K_F6,_KEYBOARD]
KEY_F7 = [pygame.K_F7,_KEYBOARD]
KEY_F8 = [pygame.K_F8,_KEYBOARD]
KEY_F9 = [pygame.K_F9,_KEYBOARD]
KEY_F10 = [pygame.K_F10,_KEYBOARD]
KEY_F11 = [pygame.K_F11,_KEYBOARD]
KEY_F12 = [pygame.K_F12,_KEYBOARD]
KEY_ARROW_LEFT = [pygame.K_LEFT,_KEYBOARD]
KEY_ARROW_RIGHT = [pygame.K_RIGHT,_KEYBOARD]
KEY_ARROW_UP = [pygame.K_UP,_KEYBOARD]
KEY_ARROW_DOWN = [pygame.K_DOWN,_KEYBOARD]
KEY_RETURN = [pygame.K_RETURN,_KEYBOARD]
KEY_SPACE = [pygame.K_SPACE,_KEYBOARD]
KEY_ESCAPE = [pygame.K_ESCAPE,_KEYBOARD]
KEY_BACKSPACE = [pygame.K_BACKSPACE,_KEYBOARD]

# Mouse input index
MOUSE_LEFTCLICK = [0,_MOUSE]
MOUSE_MIDDLECLICK = [1,_MOUSE]
MOUSE_RIGHTCLICK = [2,_MOUSE]

# Joystick input index
JOYSTICK_BUTTON_DOWN = [0,_JOYSTICK]
JOYSTICK_BUTTON_RIGHT = [1,_JOYSTICK]
JOYSTICK_BUTTON_UP = [2,_JOYSTICK]
JOYSTICK_BUTTON_LEFT = [3,_JOYSTICK]
JOYSTICK_DPAD_DOWN = [4,_JOYSTICK]
JOYSTICK_DPAD_RIGHT = [5,_JOYSTICK]
JOYSTICK_DPAD_UP = [6,_JOYSTICK]
JOYSTICK_DPAD_LEFT = [7,_JOYSTICK]
JOYSTICK_RIGHT_STICK_VERTICAL = [8,_JOYSTICK]
JOYSTICK_RIGHT_STICK_HORIZONTAL = [9,_JOYSTICK]
JOYSTICK_RIGHT_STICK = [10,_JOYSTICK]
JOYSTICK_LEFT_STICK_VERTICAL = [11,_JOYSTICK]
JOYSTICK_LEFT_STICK_HORIZONTAL = [12,_JOYSTICK]
JOYSTICK_LEFT_STICK = [13,_JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_1 = [14,_JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_2 = [15,_JOYSTICK]
JOYSTICK_RIGHT_BUMPER = [16,_JOYSTICK]
JOYSTICK_LEFT_BUMPER = [17,_JOYSTICK]
JOYSTICK_TRIGGER_R2 = [18,_JOYSTICK]
JOYSTICK_TRIGGER_L2 = [19,_JOYSTICK]
JOYSTICK_LEFT_STICK_UP = [20,_JOYSTICK]
JOYSTICK_LEFT_STICK_DOWN = [21,_JOYSTICK]
JOYSTICK_LEFT_STICK_LEFT = [22,_JOYSTICK]
JOYSTICK_LEFT_STICK_RIGHT = [23,_JOYSTICK]
JOYSTICK_RIGHT_STICK_UP = [24,_JOYSTICK]
JOYSTICK_RIGHT_STICK_DOWN = [25,_JOYSTICK]
JOYSTICK_RIGHT_STICK_LEFT = [26,_JOYSTICK]
JOYSTICK_RIGHT_STICK_RIGHT = [27,_JOYSTICK]

# Joystick types
_XBOX_360_CONTROLLER = 0
_PLAYSTATION_4_CONTROLLER = 1
_PLAYSTATION_5_CONTROLLER = 2
_NINTENDO_SWITCH_PRO_CONTROLLER = 3
_NINTENDO_SWITCH_JOYCON_CONTROLLER_L = 4
_NINTENDO_SWITCH_JOYCON_CONTROLLER_R = 5
_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R = 6

# Joystick button maps
_JOYSTICK_XBOX_360_BUTTON_MAP = [
    
    [JOYSTICK_BUTTON_DOWN],         # A BUTTON
    [JOYSTICK_BUTTON_RIGHT],        # B BUTTON
    [JOYSTICK_BUTTON_LEFT],         # X BUTTON
    [JOYSTICK_BUTTON_UP],           # Y BUTTON
    [JOYSTICK_LEFT_BUMPER],         # LEFT BUMPER
    [JOYSTICK_RIGHT_BUMPER],        # RIGHT BUMPER
    [JOYSTICK_BUTTON_SPECIAL_1],    # BACK BUTTON 
    [JOYSTICK_BUTTON_SPECIAL_2],    # START BUTTON
    [JOYSTICK_LEFT_STICK],          # LEFT STICK
    [JOYSTICK_RIGHT_STICK],         # RIGHT STICK
    [JOYSTICK_BUTTON_SPECIAL_1],    # PS BUTTON
]

_JOYSTICK_PLAYSTATION_BUTTON_MAP = [
    [JOYSTICK_BUTTON_DOWN],         # CROSS BUTTON
    [JOYSTICK_BUTTON_RIGHT],        # CIRCLE BUTTON
    [JOYSTICK_BUTTON_UP],           # TRIANGLE BUTTON
    [JOYSTICK_BUTTON_LEFT],         # SQUARE BUTTON
    [JOYSTICK_BUTTON_SPECIAL_1],    # SHARE BUTTON  
    [JOYSTICK_BUTTON_SPECIAL_1],    # PS BUTTON
    [JOYSTICK_BUTTON_SPECIAL_2],    # OPTIONS BUTTON
    [JOYSTICK_LEFT_STICK],          # LEFT STICK
    [JOYSTICK_RIGHT_STICK],         # RIGHT STICK
    [JOYSTICK_LEFT_BUMPER],         # LEFT BUMPER
    [JOYSTICK_RIGHT_BUMPER],        # RIGHT BUMPER
    [JOYSTICK_DPAD_UP],             # DPAD UP
    [JOYSTICK_DPAD_DOWN],           # DPAD DOWN
    [JOYSTICK_DPAD_LEFT],           # DPAD LEFT
    [JOYSTICK_DPAD_RIGHT],          # DPAD RIGHT
    [JOYSTICK_BUTTON_SPECIAL_2],    # TOUCH PAD
]

_JOYSTICK_NINTENDO_SWITCH_PRO_CONTROLLER_BUTTON_MAP = [
    [JOYSTICK_BUTTON_RIGHT],        # A BUTTON
    [JOYSTICK_BUTTON_DOWN],         # B BUTTON
    [JOYSTICK_BUTTON_UP],           # X BUTTON
    [JOYSTICK_BUTTON_LEFT],         # Y BUTTON
    [JOYSTICK_BUTTON_SPECIAL_1],    # - BUTTON  
    [JOYSTICK_BUTTON_SPECIAL_1],    # HOME BUTTON
    [JOYSTICK_BUTTON_SPECIAL_2],    # + BUTTON
    [JOYSTICK_LEFT_STICK],          # LEFT STICK
    [JOYSTICK_RIGHT_STICK],         # RIGHT STICK
    [JOYSTICK_LEFT_BUMPER],         # LEFT BUMPER
    [JOYSTICK_RIGHT_BUMPER],        # RIGHT BUMPER
    [JOYSTICK_DPAD_UP],             # DPAD UP
    [JOYSTICK_DPAD_DOWN],           # DPAD DOWN
    [JOYSTICK_DPAD_LEFT],           # DPAD LEFT
    [JOYSTICK_DPAD_RIGHT],          # DPAD RIGHT
    [JOYSTICK_BUTTON_SPECIAL_2],    # CAPTURE BUTTON
]

_JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_BUTTON_MAP = [
    [JOYSTICK_BUTTON_RIGHT],        # DPAD RIGHT
    [JOYSTICK_BUTTON_DOWN],         # DPAD DOWN
    [JOYSTICK_BUTTON_UP],           # DPAD UP
    [JOYSTICK_BUTTON_LEFT],         # DPAD LEFT
    [None],
    [JOYSTICK_BUTTON_SPECIAL_2],    # CAPTURE BUTTON
    [JOYSTICK_BUTTON_SPECIAL_1],    # - BUTTON
    [JOYSTICK_LEFT_STICK],          # LEFT STICK
    [None],
    [JOYSTICK_LEFT_BUMPER],         # SL
    [JOYSTICK_RIGHT_BUMPER],        # SR
    [None],
    [None],
    [None],
    [None],
    [None],
    [None],
    [JOYSTICK_TRIGGER_L2],          # L 
    [None],
    [JOYSTICK_TRIGGER_L2],          # ZL
]

_JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_R_BUTTON_MAP = [
    [JOYSTICK_BUTTON_UP],           # X BUTTON
    [JOYSTICK_BUTTON_RIGHT],        # A BUTTON
    [JOYSTICK_BUTTON_LEFT],         # Y BUTTON
    [JOYSTICK_BUTTON_DOWN],         # B BUTTON
    [None],
    [JOYSTICK_BUTTON_SPECIAL_1],    # HOME BUTTON
    [JOYSTICK_BUTTON_SPECIAL_2],    # + BUTTON
    [JOYSTICK_RIGHT_STICK],         # RIGHT STICK
    [None],
    [JOYSTICK_LEFT_BUMPER],         # SL
    [JOYSTICK_RIGHT_BUMPER],        # SR
    [None],
    [None],
    [None],
    [None],
    [None],
    [JOYSTICK_TRIGGER_R2],          # R
    [None],
    [JOYSTICK_TRIGGER_R2],          # ZR
    [None],
]

_JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R_BUTTON_MAP = [
    [JOYSTICK_BUTTON_RIGHT],        # A BUTTON
    [JOYSTICK_BUTTON_DOWN],         # B BUTTON
    [JOYSTICK_BUTTON_UP],           # X BUTTON
    [JOYSTICK_BUTTON_LEFT],         # Y BUTTON
    [JOYSTICK_BUTTON_SPECIAL_1],    # - BUTTON  
    [JOYSTICK_BUTTON_SPECIAL_1],    # HOME BUTTON
    [JOYSTICK_BUTTON_SPECIAL_2],    # + BUTTON
    [JOYSTICK_LEFT_STICK],          # LEFT STICK
    [JOYSTICK_RIGHT_STICK],         # RIGHT STICK
    [JOYSTICK_LEFT_BUMPER],         # LEFT BUMPER
    [JOYSTICK_RIGHT_BUMPER],        # RIGHT BUMPER
    [JOYSTICK_DPAD_UP],             # DPAD UP
    [JOYSTICK_DPAD_DOWN],           # DPAD DOWN
    [JOYSTICK_DPAD_LEFT],           # DPAD LEFT
    [JOYSTICK_DPAD_RIGHT],          # DPAD RIGHT
    [JOYSTICK_BUTTON_SPECIAL_2],    # CAPTURE BUTTON
]

_JOYSTICK_BUTTON_MAP = [
    _JOYSTICK_XBOX_360_BUTTON_MAP,
    _JOYSTICK_PLAYSTATION_BUTTON_MAP,
    _JOYSTICK_PLAYSTATION_BUTTON_MAP,
    _JOYSTICK_NINTENDO_SWITCH_PRO_CONTROLLER_BUTTON_MAP,
    _JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_BUTTON_MAP,
    _JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_R_BUTTON_MAP,
    _JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R_BUTTON_MAP,
]

# Joystick axis map

_JOYSTICK_GENERIC_AXIS_MAP = [
    JOYSTICK_LEFT_STICK_HORIZONTAL,
    JOYSTICK_LEFT_STICK_VERTICAL,
    JOYSTICK_RIGHT_STICK_HORIZONTAL,
    JOYSTICK_RIGHT_STICK_VERTICAL,
    JOYSTICK_TRIGGER_L2,
    JOYSTICK_TRIGGER_R2,
]

_JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_AXIS_MAP = [
    JOYSTICK_LEFT_STICK_VERTICAL,
    JOYSTICK_LEFT_STICK_HORIZONTAL,
]

_JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_R_AXIS_MAP = [
    JOYSTICK_RIGHT_STICK_VERTICAL,
    JOYSTICK_RIGHT_STICK_HORIZONTAL,
]

_JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R_AXIS_MAP = [
    JOYSTICK_LEFT_STICK_HORIZONTAL,
    JOYSTICK_LEFT_STICK_VERTICAL,
    JOYSTICK_RIGHT_STICK_HORIZONTAL,
    JOYSTICK_RIGHT_STICK_VERTICAL,
]

_JOYSTICK_AXIS_MAP = [
    _JOYSTICK_GENERIC_AXIS_MAP,
    _JOYSTICK_GENERIC_AXIS_MAP,
    _JOYSTICK_GENERIC_AXIS_MAP,
    _JOYSTICK_GENERIC_AXIS_MAP,
    _JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_AXIS_MAP,
    _JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_R_AXIS_MAP,
    _JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R_AXIS_MAP,
]

_JOYSTICK_GENERIC_DIRECTION_AXIS_MAP = [
    [JOYSTICK_LEFT_STICK_LEFT,JOYSTICK_LEFT_STICK_RIGHT],
    [JOYSTICK_LEFT_STICK_UP,JOYSTICK_LEFT_STICK_DOWN],
    [JOYSTICK_RIGHT_STICK_LEFT,JOYSTICK_RIGHT_STICK_RIGHT],
    [JOYSTICK_RIGHT_STICK_UP,JOYSTICK_RIGHT_STICK_DOWN],
    [JOYSTICK_TRIGGER_L2,JOYSTICK_TRIGGER_L2],
    [JOYSTICK_TRIGGER_R2,JOYSTICK_TRIGGER_R2],
]

_JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_DIRECTION_AXIS_MAP = [
    [JOYSTICK_LEFT_STICK_LEFT,JOYSTICK_LEFT_STICK_RIGHT],
    [JOYSTICK_LEFT_STICK_UP,JOYSTICK_LEFT_STICK_DOWN],
]

_JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_R_DIRECTION_AXIS_MAP = [
    [JOYSTICK_RIGHT_STICK_LEFT,JOYSTICK_RIGHT_STICK_RIGHT],
    [JOYSTICK_RIGHT_STICK_UP,JOYSTICK_RIGHT_STICK_DOWN],
]

_JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R_DIRECTION_AXIS_MAP = [
    [JOYSTICK_LEFT_STICK_LEFT,JOYSTICK_LEFT_STICK_RIGHT],
    [JOYSTICK_LEFT_STICK_UP,JOYSTICK_LEFT_STICK_DOWN],
    [JOYSTICK_RIGHT_STICK_LEFT,JOYSTICK_RIGHT_STICK_RIGHT],
    [JOYSTICK_RIGHT_STICK_UP,JOYSTICK_RIGHT_STICK_DOWN],
]

_JOYSTICK_DIRECTION_AXIS_MAP = [
    _JOYSTICK_GENERIC_DIRECTION_AXIS_MAP,
    _JOYSTICK_GENERIC_DIRECTION_AXIS_MAP,
    _JOYSTICK_GENERIC_DIRECTION_AXIS_MAP,
    _JOYSTICK_GENERIC_DIRECTION_AXIS_MAP,
    _JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_DIRECTION_AXIS_MAP,
    _JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_R_DIRECTION_AXIS_MAP,
    _JOYSTICK_NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R_DIRECTION_AXIS_MAP,
]

class Input:
    def __init__(self, engine, joystick_dead_zone:int=0.15) -> None:

        """
        Initialise the engines input system.

        The input system should help collect and read out many inputs by a specified key.

        Args:
        
        - engine (Engine): The engine to access specific variables.
        - joystick_dead_zone (int)=0.15: Default controller stick deadzone.

        !!!This is only used internally by the engine and should not be called in a game!!!
        """

        # Engine variable
        self._engine = engine

        # Mouse variables        
        self.mouse = self._Mouse()

        # Keyboard variables
        self._keys = {}
        self._reset_keys = []
        
        # Joystick variables
        self.joystick_dead_zone = joystick_dead_zone
        self._joystick_devices = []
        self._reset_joy = []
        
        # Input variables
        self.autosave = True
        self.save_path = os.path.join("data","saves","input")
        self._registered_input = {
            "accept":[[MOUSE_LEFTCLICK,CLICKED],[KEY_SPACE,CLICKED],[KEY_RETURN,CLICKED],[JOYSTICK_BUTTON_DOWN,CLICKED]],
            "cancel":[[KEY_ESCAPE,CLICKED],[KEY_BACKSPACE,CLICKED],[JOYSTICK_BUTTON_RIGHT,CLICKED]],
            "right":[[KEY_D,PRESSED],[KEY_L,PRESSED],[KEY_ARROW_RIGHT,PRESSED],[JOYSTICK_DPAD_RIGHT,PRESSED],[JOYSTICK_LEFT_STICK_RIGHT,PRESSED],[JOYSTICK_RIGHT_STICK_RIGHT,PRESSED]],
            "left":[[KEY_A,PRESSED],[KEY_J,PRESSED],[KEY_ARROW_LEFT,PRESSED],[JOYSTICK_DPAD_LEFT,PRESSED],[JOYSTICK_LEFT_STICK_LEFT,PRESSED],[JOYSTICK_RIGHT_STICK_LEFT,PRESSED]],
            "up":[[KEY_W,PRESSED],[KEY_I,PRESSED],[KEY_ARROW_UP,PRESSED],[JOYSTICK_DPAD_UP,PRESSED],[JOYSTICK_LEFT_STICK_UP,PRESSED],[JOYSTICK_RIGHT_STICK_UP,PRESSED]],
            "down":[[KEY_S,PRESSED],[KEY_K,PRESSED],[KEY_ARROW_DOWN,PRESSED],[JOYSTICK_DPAD_DOWN,PRESSED],[JOYSTICK_LEFT_STICK_DOWN,PRESSED],[JOYSTICK_RIGHT_STICK_DOWN,PRESSED]],
            "screenshot":[[KEY_P,CLICKED],[KEY_F6,CLICKED]]
        }

        # Setting default value for keys
        for i in self._registered_input:
            for key in self._registered_input[i]:
                if key[0][1] == _KEYBOARD:
                    self._keys[key[0][0]] = [False,False,False]

    def new(self, name:str, key:list[int,int], method:int=1) -> bool:

        """
        Register or add a new input for read out later.
        
        Args:
        - name (str): The name of the input to register.
        - key: The input key which will be monitored.
        - method: The way the input is pressed: [CLICKED, PRESSED, RELEASE].
        
        Returns:
        - True if registration was successful.
        - False if input is already registered or something went wrong.

        If the variable autosave is True the new input is automatically saved and loaded.

        Example:
        ```
        self.input.new("move_left",KEY_ARROW_LEFT,PRESSED)
        ```
        """

        # Register/add new input
        try:
            if name not in self._registered_input:
                self._registered_input[name] = [[key,method]]
            else:
                if [key,method] not in self.registered_input[name]:
                    self._registered_input[name].append([key,method])
                else:
                    return False

            self._keys[key[0]] = [False,False,False]
            if self.autosave:
                self.save()
                self.load()
            return True
        except:
            return False

        
    def remove(self, inputname:str) -> bool:

        """ 
        Removes registered input.

        Args:
        - inputname (str): the name of the registered input to remove.
        
        Returns:
        - True if removal was successful.
        - False if something went wrong.
        
        If the variable autosave is True the removal of the input is automatically saved.

        Example:

        ```
        self.input.remove("move_left")
        ```
        registered inputs 

        - before removal:
        {"accept","cancel","right","left","up","down","screenshot","move_left"}

        - after removal:
        {"accept","cancel","right","left","up","down","screenshot"}
        """

        # Remove registered input
        try:
            del self._registered_input[inputname]
            if self.autosave:
                self.save()
                self.load()
            return True
        except:
            return False

    def reset(self, name:str, controller_index:int=-1):

        """
        Resets input to default value.
        
        Args:
        - name (str): The name of the input value to reset.
        - controller_index (int): Index or joystick id of the controller to reset.
        
        Returns:
        - True if reset was successful.
        - False if controller_index is out of range or something went wrong.

        Example:

        ```
        print(self.input.get("move_left"))
        >>> 1
        self.input.reset("move_left")
        print(self.input.get("move_left"))
        >>> 0
        ```
        """

        # Resets value of registered input to default

        try:
            for key in self._registered_input[name]:
                if key[0][1] == _KEYBOARD:
                    self._keys[key[0][0]] = [False,False,False]
                    
                # Mouse values
                elif key[0][1] == _MOUSE:
                    self.mouse.buttons[key[0][0]] = [False,False,False]
                    
                # Joystick values
                elif key[0][1] == _JOYSTICK:
                    if controller_index == -1:

                        # Resets value from all joysticks
                        for i in range(len(self._joystick_devices)):
                            self._joystick_devices[controller_index].inputs[key[0][0]] = [False,False,False]
                    else:

                        # Resets value from specified joystick
                        if controller_index < len(self._joystick_devices):
                            self._joystick_devices[controller_index].inputs[key[0][0]] = [False,False,False]
                        else:
                            return False
            return True
        except:
            return False
        
    def get(self, name:str, controller_index:int=-1) -> int|float:

        """
        Gets value of registered input.

        Args:
        - name (str): The name of the registered input to get a value from.
        - controller_index (int): Index or joystick id of the controller to get a value from.
        
        Returns:
        - Axis return value between -1.0 and 1.0.
        - Keys and buttons return either 0 or 1.
        - If return is 0 either the inputname or joystick dose not exist or input is on default value.

        Example:

        ```
        print(self.input.get("move_left"))
        >>> 1
        ```
        """

        # Get input value from registered input
        try:
            for key in self._registered_input[name]:

                # Keyboard values
                if key[0][1] == _KEYBOARD:
                    if self._keys[key[0][0]][key[1]]:
                        return 1

                # Mouse values
                elif key[0][1] == _MOUSE:
                    if self.mouse.buttons[key[0][0]][key[1]]:
                        return 1

                # Joystick values
                elif key[0][1] == _JOYSTICK:
                    if controller_index == -1:

                        # Get value from not specified joystick
                        for i in range(len(self._joystick_devices)):
                            input_value = self._joystick_devices[i].get_input(key[0][0],key[1])
                            if input_value != False or input_value != 0.0:
                                return input_value
                    else:

                        # Get value from specified joystick
                        if controller_index < len(self._joystick_devices):
                            input_value = self._joystick_devices[controller_index].get_input(key[0][0],key[1])
                        else:
                            return 0

                        # Filter joystick input value
                        if input_value != False or input_value != 0.0:
                            return input_value
        except:
            return 0

        return 0
    
    def set(self, name:str, keys:list[int,int]):

        """
        Register or add a new input to read out later.
        
        Args:
        - name (str): The name of the input to overwrite.
        - keys (list): Is a list of [key, method].
        - method: The way the input is pressed: [CLICKED, PRESSED, RELEASE].
        
        Returns:
        - True if registration was successful.
        - False if something went wrong.

        If the variable autosave is True the new input is automatically saved and loaded.

        Example:
        ```
        self.input.set("move_left",[[KEY_D,PRESSED],[KEY_ARROW_LEFT,PRESSED]])
        ```
        """

        # Sets key to new inputs
        try:
            self._registered_input[name] = key
            for key in self._registered_input[name]:
                if key[0][1] == _KEYBOARD:
                    self._keys[key[0][0]] = [False,False,False]

            if self.autosave:
                self.save()
                self.load()

            return True
        except:
            return False
    
    def save(self):

        """
        Saves registered inputs to file.
        
        Args:
        - no args are required.

        Returns:
        - True if save was successful.
        - False if something went wrong.

        Example:
        ```
        self.input.save()
        ```
        """

        # Save registered input in file
        try:
            with open(self.save_path,"w+") as f:
                json.dump(self._registered_input,f)
            return True
        except:
            return False

    def load(self):

        """
        Load registered inputs from file.
        
        Args:
        - no args are required.

        Returns:
        - True if load was successful.
        - False if something went wrong.

        Example:
        ```
        self.input.load()
        ```
        """

        # Load registered input in file
        try:
            with open(self.save_path,"r+") as f:
                self._registered_input = json.load(f)

                # Setting default value for keys
                for i in self._registered_input:
                    for key in self._registered_input[i]:
                        if key[0][1] == _KEYBOARD:
                            self._keys[key[0][0]] = [False,False,False]
            return True
        except:
            return False
        
    def _update(self) -> None:

        # Update all input devices
        for key in self._reset_keys.copy():
            self._keys[key][0] = False
            self._keys[key][2] = False
            self._reset_keys.remove(key)

        self.mouse._update()

        for joystick in self._reset_joy.copy():
            joystick.reset()
            self._reset_joy.remove(joystick)

    def _handle_key_event(self, event:pygame.Event):

        # Handel joystick button down event
        if event.type == pygame.KEYDOWN:
            self._keys[event.key] = [True,True,False]
            self._reset_keys.append(event.key)

        # Handel mouse button release event
        elif event.type == pygame.KEYUP:
            self._keys[event.key] = [False,False,True]
            self._reset_keys.append(event.key)

    def _handle_mouse_event(self, event:pygame.Event):
        # Handel joystick button down event
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse.buttons[event.button-1] = [True,True,False]

        # Handel mouse button release event
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouse.buttons[event.button-1] = [False,False,True]

    def _handle_joy_event(self, event:pygame.Event):

        # joystick specification
        joy_index = event.joy
        joy_type = self._joystick_devices[joy_index].type
        
        # Handel joystick button click event
        if event.type == pygame.JOYBUTTONDOWN:
            button_index = event.button
            self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][button_index][0][0]] = [True,True,False]
            self._reset_joy.append(self._joystick_devices[joy_index])

        # Handel joystick button release event
        elif event.type == pygame.JOYBUTTONUP:
            button_index = event.button
            self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][button_index][0][0]] = [False,False,True]
            self._reset_joy.append(self._joystick_devices[joy_index])
            
        # Handel joystick axis movement event
        elif event.type == pygame.JOYAXISMOTION:
            axis_index = event.axis
            value = 0.0

            # Detect deadzone
            if abs(event.value) > self.joystick_dead_zone:
                value = max(min(event.value,1),-1)
            self._joystick_devices[joy_index].inputs[_JOYSTICK_AXIS_MAP[joy_type][axis_index][0]] = value

            # Direction inputs

            self._joystick_devices[joy_index].inputs[_JOYSTICK_DIRECTION_AXIS_MAP[joy_type][axis_index][0][0]] = -min(value,0.0)
            self._joystick_devices[joy_index].inputs[_JOYSTICK_DIRECTION_AXIS_MAP[joy_type][axis_index][1][0]] = max(value,0.0)

        elif event.type == pygame.JOYHATMOTION:

            # Xbox dpad hat event

            # DPAD LEFT
            if event.value[0] == -1:
                self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_LEFT[0]][0][0]] = [True,True,False]
                self._reset_joy.append(self._joystick_devices[joy_index])

            # DPAD RIGHT
            elif event.value[0] == 1:
                self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_RIGHT[0]][0][0]] = [True,True,False]
                self._reset_joy.append(self._joystick_devices[joy_index])

            # DPAD resets to default
            else:
                if self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_RIGHT[0]][0][0]][1] == True:
                    self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_RIGHT[0]][0][0]] = [False,False,True]
                elif self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_LEFT[0]][0][0]][1] == True:
                    self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_LEFT[0]][0][0]] = [False,False,True]
                self._reset_joy.append(self._joystick_devices[joy_index])

            # DPAD DOWN
            if event.value[1] == -1:
                self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_DOWN[0]][0][0]] = [True,True,False]
                self._reset_joy.append(self._joystick_devices[joy_index])
            
            # DPAD UP
            elif event.value[1] == 1:
                self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_UP[0]][0][0]] = [True,True,False]
                self._reset_joy.append(self._joystick_devices[joy_index])

            # DPAD resets to default
            else:
                if self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_UP[0]][0][0]][1] == True:
                    self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_UP[0]][0][0]] = [False,False,True]
                elif self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_DOWN[0]][0][0]][1] == True:
                    self._joystick_devices[joy_index].inputs[_JOYSTICK_BUTTON_MAP[joy_type][JOYSTICK_DPAD_DOWN[0]][0][0]] = [False,False,True]
                self._reset_joy.append(self._joystick_devices[joy_index])

    def _init_joysticks(self) -> None:

        # Creates joystick device to be used
        self._joystick_devices = []
        for joystick in range(pygame.joystick.get_count()):
            self._joystick_devices.append(self._Joystick(pygame.joystick.Joystick(joystick)))

    class _Mouse:
        def __init__(self) -> None:

            # Mouse variables
            self.position = [0,0]
            self.buttons = [
                [False,False,False],
                [False,False,False],
                [False,False,False]
            ]

        def _update(self) -> None:

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

        def get_pos(self) -> list[int,int]:

            """
            Returns mouse position relative to main window.
            
            Args:
            - no args are required.

            Returns:
            - List of [x mouse position (int), y mouse position (int)].

            Example:
            ```
            mouse_pos = self.input.mouse.get_pos()
            ```
            """

            # Getting mouse position
            return self.position

    class _Joystick:
        def __init__(self, joystick:pygame.joystick.JoystickType) -> None:

            # Joystick variables
            self.joystick = joystick
            self.name = joystick.get_name()
            if self.name == "Xbox 360 Controller":
                self.type = _XBOX_360_CONTROLLER
            elif self.name == "PS4 Controller":
                self.type = _PLAYSTATION_4_CONTROLLER
            elif self.name == "Sony Interactive Entertainment Wireless Controller":
                self.type = _PLAYSTATION_5_CONTROLLER
            elif self.name == "Nintendo Switch Pro Controller":
                self.type = _NINTENDO_SWITCH_PRO_CONTROLLER
            elif self.name == "Nintendo Switch Joy-Con (L)":
                self.type = _NINTENDO_SWITCH_JOYCON_CONTROLLER_L
            elif self.name == "Nintendo Switch Joy-Con (R)":
                self.type = _NINTENDO_SWITCH_JOYCON_CONTROLLER_R
            elif self.name == "Nintendo Switch Joy-Con (L/R)":
                self.type = _NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R
            else:
                self.type = _XBOX_360_CONTROLLER
            self.battery = joystick.get_power_level()
            self.device_id = joystick.get_id()
            self.instance_id = joystick.get_instance_id()
            self.guid = joystick.get_guid()
            self.inputs = [
                [False,False,False],    # JOYSTICK_BUTTON_DOWN
                [False,False,False],    # JOYSTICK_BUTTON_RIGHT
                [False,False,False],    # JOYSTICK_BUTTON_UP
                [False,False,False],    # JOYSTICK_BUTTON_LEFT
                [False,False,False],    # JOYSTICK_DPAD_DOWN
                [False,False,False],    # JOYSTICK_DPAD_RIGHT
                [False,False,False],    # JOYSTICK_DPAD_UP
                [False,False,False],    # JOYSTICK_DPAD_LEFT
                0.0,                    # JOYSTICK_RIGHT_STICK_VERTICAL 
                0.0,                    # JOYSTICK_RIGHT_STICK_HORIZONTAL
                [False,False,False],    # JOYSTICK_RIGHT_STICK_CLICKED
                0.0,                    # JOYSTICK_LEFT_STICK_VERTICAL 
                0.0,                    # JOYSTICK_LEFT_STICK_HORIZONTAL
                [False,False,False],    # JOYSTICK_LEFT_STICK_CLICKED
                [False,False,False],    # JOYSTICK_BUTTON_SPEC_1
                [False,False,False],    # JOYSTICK_BUTTON_SPEC_2
                [False,False,False],    # JOYSTICK_RIGHT_BUMPER
                [False,False,False],    # JOYSTICK_LEFT_BUMPER
                0.0,                    # JOYSTICK_TRIGGER_R2
                0.0,                    # JOYSTICK_TRIGGER_L2
                0.0,                    # JOYSTICK_LEFT_STICK_UP
                0.0,                    # JOYSTICK_LEFT_STICK_DOWN
                0.0,                    # JOYSTICK_LEFT_STICK_LEFT
                0.0,                    # JOYSTICK_LEFT_STICK_RIGHT
                0.0,                    # JOYSTICK_RIGHT_STICK_UP
                0.0,                    # JOYSTICK_RIGHT_STICK_DOWN
                0.0,                    # JOYSTICK_RIGHT_STICK_LEFT
                0.0,                    # JOYSTICK_RIGHT_STICK_RIGHT
            ]

        def _reset(self) -> None:

            # Reset joystick button click and release values
            self.inputs[JOYSTICK_BUTTON_DOWN[0]][0] = False
            self.inputs[JOYSTICK_BUTTON_DOWN[0]][2] = False
            self.inputs[JOYSTICK_BUTTON_RIGHT[0]][0] = False
            self.inputs[JOYSTICK_BUTTON_RIGHT[0]][2] = False
            self.inputs[JOYSTICK_BUTTON_UP[0]][0] = False
            self.inputs[JOYSTICK_BUTTON_UP[0]][2] = False
            self.inputs[JOYSTICK_BUTTON_LEFT[0]][0] = False
            self.inputs[JOYSTICK_BUTTON_LEFT[0]][2] = False
            self.inputs[JOYSTICK_DPAD_DOWN[0]][0] = False
            self.inputs[JOYSTICK_DPAD_DOWN[0]][2] = False
            self.inputs[JOYSTICK_DPAD_RIGHT[0]][0] = False
            self.inputs[JOYSTICK_DPAD_RIGHT[0]][2] = False
            self.inputs[JOYSTICK_DPAD_UP[0]][0] = False
            self.inputs[JOYSTICK_DPAD_UP[0]][2] = False
            self.inputs[JOYSTICK_DPAD_LEFT[0]][0] = False
            self.inputs[JOYSTICK_DPAD_LEFT[0]][2] = False
            self.inputs[JOYSTICK_RIGHT_STICK[0]][0] = False
            self.inputs[JOYSTICK_RIGHT_STICK[0]][2] = False
            self.inputs[JOYSTICK_LEFT_STICK[0]][0] = False
            self.inputs[JOYSTICK_LEFT_STICK[0]][2] = False
            self.inputs[JOYSTICK_BUTTON_SPECIAL_1[0]][0] = False
            self.inputs[JOYSTICK_BUTTON_SPECIAL_1[0]][2] = False
            self.inputs[JOYSTICK_BUTTON_SPECIAL_2[0]][0] = False
            self.inputs[JOYSTICK_BUTTON_SPECIAL_2[0]][2] = False
            self.inputs[JOYSTICK_RIGHT_BUMPER[0]][0] = False
            self.inputs[JOYSTICK_RIGHT_BUMPER[0]][2] = False
            self.inputs[JOYSTICK_LEFT_BUMPER[0]][0] = False
            self.inputs[JOYSTICK_LEFT_BUMPER[0]][2] = False

        def _get_input(self, button:int, method:int) -> int|float:

            # Get joystick button value
            if type(self.inputs[button]) == list:
                return self.inputs[button][method]
            else:
                return self.inputs[button]