import pygame
from constances import *

class Input:
    def __init__(self) -> None:
        self.joystick_dead_zone = 0.15
        self.mouse_position = [0,0]
        self.mouse_left_pressed = False
        self.mouse_left_clicked = False
        self.mouse_left_released = False
        self.mouse_middle_pressed = False
        self.mouse_middle_clicked = False
        self.mouse_middle_released = False
        self.mouse_right_pressed = False
        self.mouse_right_clicked = False
        self.mouse_right_released = False

        self.joystick_devices = []

        self.joystick = [
            0, # JOYSTICK_BUTTON_DOWN
            0, # JOYSTICK_BUTTON_RIGHT
            0, # JOYSTICK_BUTTON_UP
            0, # JOYSTICK_BUTTON_LEFT
            0, # JOYSTICK_DPAD_DOWN
            0, # JOYSTICK_DPAD_RIGHT
            0, # JOYSTICK_DPAD_UP
            0, # JOYSTICK_DPAD_LEFT
            0, # JOYSTICK_RIGHT_STICK_DOWN 
            0, # JOYSTICK_RIGHT_STICK_RIGHT
            0, # JOYSTICK_RIGHT_STICK_UP
            0, # JOYSTICK_RIGHT_STICK_LEFT 
            0, # JOYSTICK_LEFT_STICK_DOWN
            0, # JOYSTICK_LEFT_STICK_RIGHT 
            0, # JOYSTICK_LEFT_STICK_UP
            0, # JOYSTICK_LEFT_STICK_LEFT
            0, # JOYSTICK_BUTTON_OPTIONS 
            0, # JOYSTICK_BUTTON_SHARE
            0, # JOYSTICK_BUTTON_TRIGGER_R1
            0, # JOYSTICK_BUTTON_TRIGGER_L1
            0, # JOYSTICK_BUTTON_TRIGGER_R2
            0, # JOYSTICK_BUTTON_TRIGGER_L2
        ]
        
        for joystick in range(pygame.joystick.get_count()):
            self.joystick_devices.append(pygame.joystick.Joystick(joystick))
            
        self.registered_input = {
            "accept":[MOUSE_CLICK_LEFT,KEY_SPACE,KEY_RETURN,JOYSTICK_BUTTON_DOWN],
            "cancel":[KEY_ESCAPE,KEY_BACKSPACE,JOYSTICK_BUTTON_RIGHT],
            "right":[KEY_D,KEY_ARROW_RIGHT,JOYSTICK_DPAD_RIGHT,JOYSTICK_LEFT_STICK_RIGHT],
            "left":[KEY_A,KEY_ARROW_LEFT,JOYSTICK_DPAD_LEFT,JOYSTICK_LEFT_STICK_LEFT],
            "up":[KEY_W,KEY_ARROW_UP,JOYSTICK_DPAD_UP,JOYSTICK_LEFT_STICK_UP],
            "down":[KEY_S,KEY_ARROW_DOWN,JOYSTICK_DPAD_DOWN,JOYSTICK_LEFT_STICK_DOWN]
        }

    def new(self,name:str,key:int):
        if name not in self._registered_input:
            self._registered_input[name] = []
        self._registered_input[name].append(key)

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

    def _update(self,engine):
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