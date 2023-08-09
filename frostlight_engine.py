import os
import time
import pygame
import logging
import argparse
import datetime
from classes.functions import *
from classes.logger import Logger
from classes.window import Window

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

        # List variables go here
        self.display_update_rects = []

        # Object variables go here
        self.clock = pygame.time.Clock()
        self.logger = Logger()
        self.window = Window()

        self.logger.info("All Engine variables were created")

        # Object processing go here
        self.window.create()
        pygame.event.set_allowed([pygame.QUIT, pygame.WINDOWMOVED, pygame.VIDEORESIZE, pygame.KEYDOWN])


    def scale_rect(rect:pygame.Rect, amount:float) -> pygame.Rect:
        w = rect.width * amount
        h = rect.height * amount
        new = pygame.Rect(0,0,w,h)
        return new
    
    def scale_sprite(sprite:pygame.Surface, amount:float) -> pygame.Rect:
        w = sprite.get_width() * amount
        h = sprite.get_height() * amount
        new = pygame.transform.scale(sprite,(w,h)).convert_alpha()
        return new
        
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
        self.logger.info("starting game")
        while self.run_game:
            try:
                self.get_events()
                self.update()
                self.draw()
            except Exception as e:
                self.logger.error(e)

    def quit(self):
        self.run_game = False

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-b", "--build", action="store_true")
    # parser.add_argument("-n", "--name", action="store_true")
    # args = parser.parse_args()
    # if args.build:
        
    #     #Build game to exe
    #     pass
    # elif args.name:
    #     pass

    # Setup new Project
    create_file_structure()