import os
import time
import pygame
import datetime
from classes.functions import *
from classes.window import Window
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("-b", "--build", action="store_true")

# args = parser.parse_args()
# print(args.build)

class Engine:
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
                 window_depth:int=16,
                 window_name:str="New Game",
                 window_size:list=[1920,1080]):
        
        # initialize all modules
        pygame.init()
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
        self.version = 0.1
        self.window_depth = window_depth

        # String variables go here
        self.game_state = "intro"
        self.game_version = game_version
        self.language = language
        self.window_name = window_name

        self.clock = pygame.time.Clock()

        self.window = Window()
        self.window.create()

        pygame.event.set_allowed([pygame.QUIT, pygame.WINDOWMOVED, pygame.VIDEORESIZE, pygame.KEYDOWN])
        
    def get_events(self):
        self.clock.tick(self.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            # Window events
            elif event.type == pygame.WINDOWMOVED:
                self.last_time = time.time()
                self.delta_time = 0

            elif event.type == pygame.VIDEORESIZE:
                if not self.fullscreen:
                    self.last_time = time.time()
                    self.delta_time = 0
                    self.window.resize([event.w,event.h])

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.window.toggle_fullscreen()

    def update(self):
        self.delta_time = time.time()-self.last_time
        self.last_time = time.time()

    def run(self):
        log("Starting game")
        while self.run_game:
            self.get_events()
            self.update()
            self.draw()

    def quit(self):
        self.run_game = False

if __name__ == "__main__":
    create_file_structure()