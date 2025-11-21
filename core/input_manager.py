from init import *

CLICKED = 0
PRESSED = 1
RELEASED = 2

class DeviceType:
    KEYBOARD = 1
    MOUSE = 2

class InputCode:
    def __init__(self, device_type, code):
        self.device_type = device_type
        self.code = code

class KEYBOARD:
    # Letters
    A = InputCode(DeviceType.KEYBOARD, glfw.KEY_A)
    B = InputCode(DeviceType.KEYBOARD, glfw.KEY_B)
    C = InputCode(DeviceType.KEYBOARD, glfw.KEY_C)
    D = InputCode(DeviceType.KEYBOARD, glfw.KEY_D)
    E = InputCode(DeviceType.KEYBOARD, glfw.KEY_E)
    F = InputCode(DeviceType.KEYBOARD, glfw.KEY_F)
    G = InputCode(DeviceType.KEYBOARD, glfw.KEY_G)
    H = InputCode(DeviceType.KEYBOARD, glfw.KEY_H)
    I = InputCode(DeviceType.KEYBOARD, glfw.KEY_I)
    J = InputCode(DeviceType.KEYBOARD, glfw.KEY_J)
    K = InputCode(DeviceType.KEYBOARD, glfw.KEY_K)
    L = InputCode(DeviceType.KEYBOARD, glfw.KEY_L)
    M = InputCode(DeviceType.KEYBOARD, glfw.KEY_M)
    N = InputCode(DeviceType.KEYBOARD, glfw.KEY_N)
    O = InputCode(DeviceType.KEYBOARD, glfw.KEY_O)
    P = InputCode(DeviceType.KEYBOARD, glfw.KEY_P)
    Q = InputCode(DeviceType.KEYBOARD, glfw.KEY_Q)
    R = InputCode(DeviceType.KEYBOARD, glfw.KEY_R)
    S = InputCode(DeviceType.KEYBOARD, glfw.KEY_S)
    T = InputCode(DeviceType.KEYBOARD, glfw.KEY_T)
    U = InputCode(DeviceType.KEYBOARD, glfw.KEY_U)
    V = InputCode(DeviceType.KEYBOARD, glfw.KEY_V)
    W = InputCode(DeviceType.KEYBOARD, glfw.KEY_W)
    X = InputCode(DeviceType.KEYBOARD, glfw.KEY_X)
    Y = InputCode(DeviceType.KEYBOARD, glfw.KEY_Y)
    Z = InputCode(DeviceType.KEYBOARD, glfw.KEY_Z)

    # Numbers
    NUM_0 = InputCode(DeviceType.KEYBOARD, glfw.KEY_0)
    NUM_1 = InputCode(DeviceType.KEYBOARD, glfw.KEY_1)
    NUM_2 = InputCode(DeviceType.KEYBOARD, glfw.KEY_2)
    NUM_3 = InputCode(DeviceType.KEYBOARD, glfw.KEY_3)
    NUM_4 = InputCode(DeviceType.KEYBOARD, glfw.KEY_4)
    NUM_5 = InputCode(DeviceType.KEYBOARD, glfw.KEY_5)
    NUM_6 = InputCode(DeviceType.KEYBOARD, glfw.KEY_6)
    NUM_7 = InputCode(DeviceType.KEYBOARD, glfw.KEY_7)
    NUM_8 = InputCode(DeviceType.KEYBOARD, glfw.KEY_8)
    NUM_9 = InputCode(DeviceType.KEYBOARD, glfw.KEY_9)

    # Function Keys
    F1 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F1)
    F2 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F2)
    F3 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F3)
    F4 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F4)
    F5 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F5)
    F6 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F6)
    F7 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F7)
    F8 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F8)
    F9 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F9)
    F10 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F10)
    F11 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F11)
    F12 = InputCode(DeviceType.KEYBOARD, glfw.KEY_F12)

    # Arrows
    LEFT = InputCode(DeviceType.KEYBOARD, glfw.KEY_LEFT)
    RIGHT = InputCode(DeviceType.KEYBOARD, glfw.KEY_RIGHT)
    UP = InputCode(DeviceType.KEYBOARD, glfw.KEY_UP)
    DOWN = InputCode(DeviceType.KEYBOARD, glfw.KEY_DOWN)

    # Modifiers
    LEFT_SHIFT = InputCode(DeviceType.KEYBOARD, glfw.KEY_LEFT_SHIFT)
    RIGHT_SHIFT = InputCode(DeviceType.KEYBOARD, glfw.KEY_RIGHT_SHIFT)
    LEFT_CTRL = InputCode(DeviceType.KEYBOARD, glfw.KEY_LEFT_CONTROL)
    RIGHT_CTRL = InputCode(DeviceType.KEYBOARD, glfw.KEY_RIGHT_CONTROL)
    LEFT_ALT = InputCode(DeviceType.KEYBOARD, glfw.KEY_LEFT_ALT)
    RIGHT_ALT = InputCode(DeviceType.KEYBOARD, glfw.KEY_RIGHT_ALT)
    LEFT_SUPER = InputCode(DeviceType.KEYBOARD, glfw.KEY_LEFT_SUPER)
    RIGHT_SUPER = InputCode(DeviceType.KEYBOARD, glfw.KEY_RIGHT_SUPER)

    # Special Keys
    SPACE = InputCode(DeviceType.KEYBOARD, glfw.KEY_SPACE)
    ENTER = InputCode(DeviceType.KEYBOARD, glfw.KEY_ENTER)
    ESCAPE = InputCode(DeviceType.KEYBOARD, glfw.KEY_ESCAPE)
    TAB = InputCode(DeviceType.KEYBOARD, glfw.KEY_TAB)
    BACKSPACE = InputCode(DeviceType.KEYBOARD, glfw.KEY_BACKSPACE)
    INSERT = InputCode(DeviceType.KEYBOARD, glfw.KEY_INSERT)
    DELETE = InputCode(DeviceType.KEYBOARD, glfw.KEY_DELETE)
    HOME = InputCode(DeviceType.KEYBOARD, glfw.KEY_HOME)
    END = InputCode(DeviceType.KEYBOARD, glfw.KEY_END)
    PAGE_UP = InputCode(DeviceType.KEYBOARD, glfw.KEY_PAGE_UP)
    PAGE_DOWN = InputCode(DeviceType.KEYBOARD, glfw.KEY_PAGE_DOWN)
    CAPS_LOCK = InputCode(DeviceType.KEYBOARD, glfw.KEY_CAPS_LOCK)
    SCROLL_LOCK = InputCode(DeviceType.KEYBOARD, glfw.KEY_SCROLL_LOCK)
    NUM_LOCK = InputCode(DeviceType.KEYBOARD, glfw.KEY_NUM_LOCK)

    # Symbols
    MINUS = InputCode(DeviceType.KEYBOARD, glfw.KEY_MINUS)
    EQUAL = InputCode(DeviceType.KEYBOARD, glfw.KEY_EQUAL)
    LEFT_BRACKET = InputCode(DeviceType.KEYBOARD, glfw.KEY_LEFT_BRACKET)
    RIGHT_BRACKET = InputCode(DeviceType.KEYBOARD, glfw.KEY_RIGHT_BRACKET)
    BACKSLASH = InputCode(DeviceType.KEYBOARD, glfw.KEY_BACKSLASH)
    SEMICOLON = InputCode(DeviceType.KEYBOARD, glfw.KEY_SEMICOLON)
    APOSTROPHE = InputCode(DeviceType.KEYBOARD, glfw.KEY_APOSTROPHE)
    GRAVE_ACCENT = InputCode(DeviceType.KEYBOARD, glfw.KEY_GRAVE_ACCENT)
    COMMA = InputCode(DeviceType.KEYBOARD, glfw.KEY_COMMA)
    PERIOD = InputCode(DeviceType.KEYBOARD, glfw.KEY_PERIOD)
    SLASH = InputCode(DeviceType.KEYBOARD, glfw.KEY_SLASH)

    # NumPad
    NP_0 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_0)
    NP_1 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_1)
    NP_2 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_2)
    NP_3 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_3)
    NP_4 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_4)
    NP_5 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_5)
    NP_6 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_6)
    NP_7 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_7)
    NP_8 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_8)
    NP_9 = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_9)
    NP_DECIMAL = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_DECIMAL)
    NP_DIVIDE = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_DIVIDE)
    NP_MULTIPLY = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_MULTIPLY)
    NP_SUBTRACT = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_SUBTRACT)
    NP_ADD = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_ADD)
    NP_ENTER = InputCode(DeviceType.KEYBOARD, glfw.KEY_KP_ENTER)

class MOUSE:
    LEFT = InputCode(DeviceType.MOUSE, glfw.MOUSE_BUTTON_LEFT)
    RIGHT = InputCode(DeviceType.MOUSE, glfw.MOUSE_BUTTON_RIGHT)
    MIDDLE = InputCode(DeviceType.MOUSE, glfw.MOUSE_BUTTON_MIDDLE)
    SCROLL_UP = InputCode(DeviceType.MOUSE, 3)
    SCROLL_DOWN = InputCode(DeviceType.MOUSE, 4)

class Keyboard:
    def __init__(self):
        self.states = {}

    def update_key_down(self, keycode):
        state = self.states.setdefault(keycode, [False, False, False])
        state[CLICKED] = True
        state[PRESSED] = True

    def update_key_up(self, keycode):
        state = self.states.setdefault(keycode, [False, False, False])
        state[RELEASED] = True
        state[PRESSED] = False

    def reset(self):
        for state in self.states.values():
            state[CLICKED] = False
            state[RELEASED] = False

class Mouse:
    def __init__(self):
        self._states = {}
        self.position = [0, 0]
        self.scroll = [0, 0]

    def _update_button_down(self, button):
        state = self._states.setdefault(button, [False, False, False])
        state[CLICKED] = True
        state[PRESSED] = True

    def _update_button_up(self, button):
        state = self._states.setdefault(button, [False, False, False])
        state[RELEASED] = True
        state[PRESSED] = False

    def _reset(self):
        for state in self._states.values():
            state[CLICKED] = False
            state[RELEASED] = False
        
        if MOUSE.SCROLL_UP.code in self._states:
            self._states[MOUSE.SCROLL_UP.code] = [False,False,False]
        if MOUSE.SCROLL_DOWN.code in self._states:
            self._states[MOUSE.SCROLL_DOWN.code] = [False,False,False]

        self.scroll = [0, 0]

class InputManager:
    def __init__(self):
        self._keyboard = Keyboard()
        self.mouse = Mouse()
        self._bindings = {}
        self._window = None

    def _register_callbacks(self,window):
        self._window = window
        glfw.set_key_callback(window, self._on_key_press)
        glfw.set_mouse_button_callback(window, self._on_mouse_button_press)
        glfw.set_cursor_pos_callback(window, self._on_mouse_move)
        glfw.set_scroll_callback(window, self._on_mouse_scroll)

    def bind(self, key:str, input_code:KEYBOARD|MOUSE, method=CLICKED|PRESSED|RELEASED):
        if key not in self._bindings:
            self._bindings[key] = []

        self._bindings[key].append((input_code, method))

    def unbind(self, key:str):
        del self._bindings[key]

    def get(self, key:str):
        for input_code, method in self._bindings.get(key, []):
            if input_code.device_type == DeviceType.KEYBOARD:
                state = self._keyboard.states.get(input_code.code, [False, False, False])
                if state[method]:
                    return 1

            if input_code.device_type == DeviceType.MOUSE:
                state = self.mouse._states.get(input_code.code, [False, False, False])
                if state[method]:
                    return 1
        return 0
    
    def _on_key_press(self, _, key, scancode, action, mods):
        if action == glfw.PRESS:
            self._keyboard.update_key_down(key)

        elif action == glfw.RELEASE:
            self._keyboard.update_key_up(key)

    def _on_mouse_button_press(self, _, button, action, mods):
        if action == glfw.PRESS:
            self.mouse._update_button_down(button)

        elif action == glfw.RELEASE:
            self.mouse._update_button_up(button)

    def _on_mouse_move(self, _, x, y):
        self.mouse.position = [x, y]

    def _on_mouse_scroll(self, _, dx, dy):
        self.mouse.scroll = [dx, dy]
        if dy > 0:
            self.mouse._states[MOUSE.SCROLL_UP.code] = [True,True,True]
        if dy < 0:
            self.mouse._states[MOUSE.SCROLL_DOWN.code] = [True,True,True]

    def _update(self):
        self._keyboard.reset()
        self.mouse._reset()
