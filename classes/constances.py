import pygame

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
MOUSE_CLICK_LEFT = [0,MOUSE]
MOUSE_CLICK_MIDDLE = [1,MOUSE]
MOUSE_CLICK_RIGHT = [2,MOUSE]
MOUSE_PRESSED_LEFT = [3,MOUSE]
MOUSE_PRESSED_MIDDLE = [4,MOUSE]
MOUSE_PRESSED_RIGHT = [5,MOUSE]
MOUSE_RELEASED_LEFT = [6,MOUSE]
MOUSE_RELEASED_MIDDLE = [7,MOUSE]
MOUSE_RELEASED_RIGHT = [8,MOUSE]
JOYSTICK_BUTTON_DOWN_CLICKED = [0,JOYSTICK]
JOYSTICK_BUTTON_DOWN_PRESSED = [1,JOYSTICK]
JOYSTICK_BUTTON_DOWN_RELEASED = [2,JOYSTICK]
JOYSTICK_BUTTON_RIGHT_CLICKED = [3,JOYSTICK]
JOYSTICK_BUTTON_RIGHT_PRESSED = [4,JOYSTICK]
JOYSTICK_BUTTON_RIGHT_RELEASED = [5,JOYSTICK]
JOYSTICK_BUTTON_UP_CLICKED = [6,JOYSTICK]
JOYSTICK_BUTTON_UP_PRESSED = [7,JOYSTICK]
JOYSTICK_BUTTON_UP_RELEASED = [8,JOYSTICK]
JOYSTICK_BUTTON_LEFT_CLICKED = [9,JOYSTICK]
JOYSTICK_BUTTON_LEFT_PRESSED = [10,JOYSTICK]
JOYSTICK_BUTTON_LEFT_RELEASED = [11,JOYSTICK]
JOYSTICK_DPAD_DOWN_CLICKED = [12,JOYSTICK]
JOYSTICK_DPAD_DOWN_PRESSED = [13,JOYSTICK]
JOYSTICK_DPAD_DOWN_RELEASED = [14,JOYSTICK]
JOYSTICK_DPAD_RIGHT_CLICKED = [15,JOYSTICK]
JOYSTICK_DPAD_RIGHT_PRESSED = [16,JOYSTICK]
JOYSTICK_DPAD_RIGHT_RELEASED = [17,JOYSTICK]
JOYSTICK_DPAD_UP_CLICKED = [18,JOYSTICK]
JOYSTICK_DPAD_UP_PRESSED = [19,JOYSTICK]
JOYSTICK_DPAD_UP_RELEASED = [20,JOYSTICK]
JOYSTICK_DPAD_LEFT_CLICKED = [21,JOYSTICK]
JOYSTICK_DPAD_LEFT_PRESSED = [22,JOYSTICK]
JOYSTICK_DPAD_LEFT_RELEASED = [23,JOYSTICK]
JOYSTICK_RIGHT_STICK_VERTICAL = [24,JOYSTICK]
JOYSTICK_RIGHT_STICK_HORIZONTAL = [25,JOYSTICK]
JOYSTICK_RIGHT_STICK_CLICKED = [26,JOYSTICK]
JOYSTICK_RIGHT_STICK_PRESSED = [27,JOYSTICK]
JOYSTICK_RIGHT_STICK_RELEASED = [28,JOYSTICK]
JOYSTICK_LEFT_STICK_VERTICAL = [29,JOYSTICK]
JOYSTICK_LEFT_STICK_HORIZONTAL = [30,JOYSTICK]
JOYSTICK_LEFT_STICK_CLICKED = [31,JOYSTICK]
JOYSTICK_LEFT_STICK_PRESSED = [32,JOYSTICK]
JOYSTICK_LEFT_STICK_RELEASED = [33,JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_1_CLICKED = [34,JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_1_PRESSED = [35,JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_1_RELEASED = [36,JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_2_CLICKED = [37,JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_2_PRESSED = [38,JOYSTICK]
JOYSTICK_BUTTON_SPECIAL_2_RELEASED = [39,JOYSTICK]
JOYSTICK_RIGHT_BUMPER_CLICKED = [40,JOYSTICK]
JOYSTICK_RIGHT_BUMPER_PRESSED = [41,JOYSTICK]
JOYSTICK_RIGHT_BUMPER_PRESSED = [42,JOYSTICK]
JOYSTICK_LEFT_BUMPER_CLICKED = [43,JOYSTICK]
JOYSTICK_LEFT_BUMPER_PRESSED = [44,JOYSTICK]
JOYSTICK_LEFT_BUMPER_PRESSED = [45,JOYSTICK]
JOYSTICK_TRIGGER_R2 = [46,JOYSTICK]
JOYSTICK_TRIGGER_L2 = [47,JOYSTICK]

XBOX_360_CONTROLLER = 0
PLAYSTATION_4_CONTROLLER = 1
PLAYSTATION_5_CONTROLLER = 2
NINTENDO_SWITCH_PRO_CONTROLLER = 3
NINTENDO_SWITCH_JOYCON_CONTROLLER_L = 4
NINTENDO_SWITCH_JOYCON_CONTROLLER_R = 5
NINTENDO_SWITCH_JOYCON_CONTROLLER_L_R = 6

JOYSTICK_XBOX_360_BUTTON_MAP = [
    [0,1,2],
    None,
    None,
    5
]
JOYSTICK_PLAYSTATION_4_BUTTON_MAP = [
    [0,1,2],    # CROSS BUTTON
    [3,4,5],    # CIRCLE BUTTON
    [9,10,11],  # TRIANGLE BUTTON
    [6,7,8],    # SQUARE BUTTON
    [34,35,36], # SHARE BUTTON  
    [34,35,36], # PS BUTTON
    [37,38,39], # OPTIONS BUTTON
    [31,32,33], # LEFT STICK
    [26,27,28], # RIGHT STICK
    [43,44,45], # LEFT BUMPER
    [40,41,42], # RIGHT BUMPER
    [18,19,20], # DPAD UP
    [12,13,14], # DPAD DOWN
    [21,22,23], # DPAD LEFT
    [15,16,17], # DPAD RIGHT
    [37,38,39], # TOUCH PAD
]
JOYSTICK_PLAYSTATION_5_BUTTON_MAP = [
    [0,1,2],    # CROSS BUTTON
    [3,4,5],    # CIRCLE BUTTON
    [9,10,11],  # TRIANGLE BUTTON
    [6,7,8],    # SQUARE BUTTON
    [34,35,36], # SHARE BUTTON  
    [34,35,36], # PS BUTTON
    [37,38,39], # OPTIONS BUTTON
    [31,32,33], # LEFT STICK
    [26,27,28], # RIGHT STICK
    [43,44,45], # LEFT BUMPER
    [40,41,42], # RIGHT BUMPER
    [18,19,20], # DPAD UP
    [12,13,14], # DPAD DOWN
    [21,22,23], # DPAD LEFT
    [15,16,17], # DPAD RIGHT
    [37,38,39], # TOUCH PAD
]

JOYSTICK_BUTTON_MAP = [
    JOYSTICK_XBOX_360_BUTTON_MAP,
    JOYSTICK_PLAYSTATION_4_BUTTON_MAP,
    JOYSTICK_PLAYSTATION_5_BUTTON_MAP
]
