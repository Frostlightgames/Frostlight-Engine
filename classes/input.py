import pygame
from constances import *

class Input:
    def __init__(self) -> None:
        self.joystick_dead_zone = 0.15
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
            "accept":[MOUSE_CLICK_LEFT,KEY_SPACE,KEY_RETURN],
            "cancel":[KEY_ESCAPE],
            "right":[KEY_D,KEY_ARROW_RIGHT],
            "left":[KEY_A,KEY_ARROW_LEFT],
            "up":[KEY_W,KEY_ARROW_UP],
            "down":[KEY_S,KEY_ARROW_DOWN]
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
            if key[1] == KEYBOARD:
                if keys[key[0]]:
                    key_pressed = 1
                    break
            elif key[1] == MOUSE:
                if mouse[key[0]]:
                    key_pressed = 1
                    break
        
        return key_pressed

    def mouse_pos(self) -> list[int,int]:
        return self.mouse_position

    def update(self):
        pygame_mouse_pressed = pygame.mouse.get_pressed()
        self._mouse_left_pressed = pygame_mouse_pressed[0]
        self._mouse_middle_pressed = pygame_mouse_pressed[1]
        self._mouse_right_pressed = pygame_mouse_pressed[2]

        self.mouse_position = pygame.mouse.get_pos()