import pygame

# Custom variables go here

# Input types
KEYBOARD = 0
MOUSE = 1
JOYSTICK = 2

# Input method
CLICKED = 0
PRESSED = 1
RELEASE = 2

# Keyboard input index
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
KEY_F1 = [pygame.K_F1,KEYBOARD]
KEY_F2 = [pygame.K_F2,KEYBOARD]
KEY_F3 = [pygame.K_F3,KEYBOARD]
KEY_F4 = [pygame.K_F4,KEYBOARD]
KEY_F5 = [pygame.K_F5,KEYBOARD]
KEY_F6 = [pygame.K_F6,KEYBOARD]
KEY_F7 = [pygame.K_F7,KEYBOARD]
KEY_F8 = [pygame.K_F8,KEYBOARD]
KEY_F9 = [pygame.K_F9,KEYBOARD]
KEY_F10 = [pygame.K_F10,KEYBOARD]
KEY_F11 = [pygame.K_F11,KEYBOARD]
KEY_F12 = [pygame.K_F12,KEYBOARD]
KEY_ARROW_LEFT = [pygame.K_LEFT,KEYBOARD]
KEY_ARROW_RIGHT = [pygame.K_RIGHT,KEYBOARD]
KEY_ARROW_UP = [pygame.K_UP,KEYBOARD]
KEY_ARROW_DOWN = [pygame.K_DOWN,KEYBOARD]
KEY_RETURN = [pygame.K_RETURN,KEYBOARD]
KEY_SPACE = [pygame.K_SPACE,KEYBOARD]
KEY_ESCAPE = [pygame.K_ESCAPE,KEYBOARD]
KEY_BACKSPACE = [pygame.K_BACKSPACE,KEYBOARD]

# Mouse input index
MOUSE_LEFTCLICK = [0,MOUSE]
MOUSE_MIDDLECLICK = [1,MOUSE]
MOUSE_RIGHTCLICK = [2,MOUSE]

# Joystick input index
JOYSTICK_BUTTON_DOWN = [0,JOYSTICK]
JOYSTICK_BUTTON_RIGHT = [1,JOYSTICK]
JOYSTICK_BUTTON_UP = [2,JOYSTICK]
JOYSTICK_BUTTON_LEFT = [3,JOYSTICK]
JOYSTICK_DPAD_DOWN = [4,JOYSTICK]
JOYSTICK_DPAD_RIGHT = [5,JOYSTICK]
JOYSTICK_DPAD_UP = [6,JOYSTICK]
JOYSTICK_DPAD_LEFT = [7,JOYSTICK]
JOYSTICK_RIGHT_STICK_VERTICAL = [8,JOYSTICK]
JOYSTICK_RIGHT_STICK_HORIZONTAL = [9,JOYSTICK]
JOYSTICK_RIGHT_STICK = [10,JOYSTICK]
JOYSTICK_LEFT_STICK_VERTICAL = [11,JOYSTICK]
JOYSTICK_LEFT_STICK_HORIZONTAL = [12,JOYSTICK]
JOYSTICK_LEFT_STICK = [13,JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_1 = [14,JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_2 = [15,JOYSTICK]
JOYSTICK_RIGHT_BUMPER = [16,JOYSTICK]
JOYSTICK_LEFT_BUMPER = [17,JOYSTICK]
JOYSTICK_TRIGGER_R2 = [18,JOYSTICK]
JOYSTICK_TRIGGER_L2 = [19,JOYSTICK]

# Joystick types
XBOX_360_CONTROLLER = 0
PLAYSTATION_4_CONTROLLER = 1
PLAYSTATION_5_CONTROLLER = 2
NINTENDO_SWITCH_PRO_CONTROLLER = 3
NINTENDO_SWITCH_JOYCON_CONTROLLER_L = 4
NINTENDO_SWITCH_JOYCON_CONTROLLER_R = 5
NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R = 6

# Joystick button maps
JOYSTICK_XBOX_360_BUTTON_MAP = [
    
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

JOYSTICK_PLAYSTATION_4_BUTTON_MAP = [
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

JOYSTICK_PLAYSTATION_5_BUTTON_MAP = [
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

JOYSTICK_NINTENDO_SWITCH_PRO_CONTROLLER_BUTTON_MAP = [
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

JOYSTICK_BUTTON_MAP = [
    JOYSTICK_XBOX_360_BUTTON_MAP,
    JOYSTICK_PLAYSTATION_4_BUTTON_MAP,
    JOYSTICK_PLAYSTATION_5_BUTTON_MAP,
    JOYSTICK_NINTENDO_SWITCH_PRO_CONTROLLER_BUTTON_MAP
]

# Joystick axis map
JOYSTICK_XBOX_360_AXIS_MAP = [
    JOYSTICK_LEFT_STICK_HORIZONTAL,
    JOYSTICK_LEFT_STICK_VERTICAL,
    JOYSTICK_TRIGGER_L2,
    JOYSTICK_RIGHT_STICK_HORIZONTAL,
    JOYSTICK_RIGHT_STICK_VERTICAL,
    JOYSTICK_TRIGGER_R2,
]

JOYSTICK_PLAYSTATION_4_AXIS_MAP= [
    JOYSTICK_LEFT_STICK_HORIZONTAL,
    JOYSTICK_LEFT_STICK_VERTICAL,
    JOYSTICK_RIGHT_STICK_HORIZONTAL,
    JOYSTICK_RIGHT_STICK_VERTICAL,
    JOYSTICK_TRIGGER_L2,
    JOYSTICK_TRIGGER_R2,
]

JOYSTICK_PLAYSTATION_5_AXIS_MAP= [
    JOYSTICK_LEFT_STICK_HORIZONTAL,
    JOYSTICK_LEFT_STICK_VERTICAL,
    JOYSTICK_RIGHT_STICK_HORIZONTAL,
    JOYSTICK_RIGHT_STICK_VERTICAL,
    JOYSTICK_TRIGGER_L2,
    JOYSTICK_TRIGGER_R2,
]

JOYSTICK_NINTENDO_SWITCH_PRO_CONTROLLER_AXIS_MAP= [
    JOYSTICK_LEFT_STICK_HORIZONTAL,
    JOYSTICK_LEFT_STICK_VERTICAL,
    JOYSTICK_RIGHT_STICK_HORIZONTAL,
    JOYSTICK_RIGHT_STICK_VERTICAL,
    JOYSTICK_TRIGGER_L2,
    JOYSTICK_TRIGGER_R2,
]

JOYSTICK_AXIS_MAP = [
    JOYSTICK_XBOX_360_AXIS_MAP,
    JOYSTICK_PLAYSTATION_4_AXIS_MAP,
    JOYSTICK_PLAYSTATION_5_AXIS_MAP,
    JOYSTICK_NINTENDO_SWITCH_PRO_CONTROLLER_AXIS_MAP
]

# Joystick hat map
NINTENDO_SWITCH_JOYCON_CONTROLLER_L_HAT_MAP = [
    JOYSTICK_LEFT_STICK_HORIZONTAL,
    JOYSTICK_LEFT_STICK_VERTICAL,
]

NINTENDO_SWITCH_JOYCON_CONTROLLER_R_HAT_MAP = [
    JOYSTICK_LEFT_STICK_HORIZONTAL,
    JOYSTICK_LEFT_STICK_VERTICAL,
]

JOYSTICK_XBOX_360_HAT_MAP = [
    [JOYSTICK_DPAD_DOWN,JOYSTICK_DPAD_UP],
    [JOYSTICK_DPAD_LEFT,JOYSTICK_DPAD_RIGHT],
]

JOYSTICK_HAT_MAP = [
    JOYSTICK_XBOX_360_HAT_MAP,
    None,
    None,
    None,
    NINTENDO_SWITCH_JOYCON_CONTROLLER_L_HAT_MAP,
    NINTENDO_SWITCH_JOYCON_CONTROLLER_R_HAT_MAP,
    None,
]