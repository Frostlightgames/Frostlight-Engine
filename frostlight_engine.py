import os
import time
import pygame
import argparse
from classes.input import Input
from classes.logger import Logger
from classes.window import Window
from classes.builder import Builder
from classes.constances import *
from nodes.playernode import *

class Engine:
    def __init__(self,
                 color_depth:int=16,
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
                 window_name:str="New Game",
                 window_size:list=None):
        
        # initialize all modules
        pygame.init()
        pygame.joystick.init()
        if sounds:
            pygame.mixer.pre_init(44100,-16,2,512)

        # Boolean variables go here
        self.run_game = True
        self.sounds = sounds

        # Integer and float variables go here
        self.fps = fps
        self.delta_time = 1
        self.last_time = time.time()
        self.version = 0.1

        # String variables go here
        self.engine_version = "1.0.1"
        self.game_state = "intro"
        self.game_version = game_version
        self.language = language

        # List variables go here
        self.display_update_rects = []

        # Object variables go here
        self.clock = pygame.time.Clock()
        self.builder = Builder(self)
        self.logger = Logger(self)
        self.input = Input(self)
        self.window = Window(self,window_size,fullscreen,resizable,nowindow,window_centered,vsync,window_name,mouse_visible,color_depth)

        # Object processing go here
        self.window.create()
        pygame.event.set_allowed([pygame.QUIT,
                                  pygame.WINDOWMOVED, 
                                  pygame.VIDEORESIZE, 
                                  pygame.KEYDOWN, 
                                  pygame.JOYBUTTONUP, 
                                  pygame.JOYBUTTONDOWN, 
                                  pygame.JOYAXISMOTION, 
                                  pygame.JOYHATMOTION, 
                                  pygame.JOYDEVICEADDED, 
                                  pygame.JOYDEVICEREMOVED])
        
    def get_events(self):
        self.clock.tick(self.fps)
        self.input.__update__()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            # Window events
            elif event.type == pygame.WINDOWMOVED:
                self.last_time = time.time()
                self.delta_time = 0

            elif event.type == pygame.VIDEORESIZE:
                if not self.window.fullscreen:
                    self.last_time = time.time()
                    self.delta_time = 0
                    self.window.resize([event.w,event.h])

            # Keyboard events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.window.toggle_fullscreen()

            # Mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.input.mouse.left_clicked = True
                elif event.button == 2:
                    self.input.mouse.middle_clicked = True
                elif event.button == 3:
                    self.input.mouse.right_clicked = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.input.mouse.left_released = True
                elif event.button == 2:
                    self.input.mouse.middle_released = True
                elif event.button == 3:
                    self.input.mouse.right_released = True

            # Joystick events
            elif event.type == pygame.JOYBUTTONDOWN:
                self.input.__handle_joy_event__(event)

            elif event.type == pygame.JOYBUTTONUP:
                self.input.__handle_joy_event__(event)

            elif event.type == pygame.JOYAXISMOTION:
                self.input.__handle_joy_event__(event)

            elif event.type == pygame.JOYHATMOTION:
                self.input.__handle_joy_event__(event)

            elif event.type == pygame.JOYDEVICEADDED:
                self.input.__init_joysticks__()

            elif event.type == pygame.JOYDEVICEREMOVED:
                self.input.__init_joysticks__()

    def engine_update(self):

        # Update that runs before normal update
        self.delta_time = time.time()-self.last_time
        self.last_time = time.time()

    def engine_draw(self):

        # Draw that runs after normal draw
        pygame.display.update()

    def run(self):

        # Starting game engine
        self.logger.info(f"Starting [Engine version {self.engine_version} | Game version {self.game_version}]")
        while self.run_game:

            # Main loop
            try:
                self.get_events()
                self.engine_update()
                self.update()
                self.draw()
                self.engine_draw()
            except Exception as e:
                
                # Error logging and catching
                self.logger.error(e)

        # Ending game
        self.logger.info("Closed game")

    def quit(self):
        self.run_game = False

if __name__ == "__main__":

    # Parser arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pack", action="store_true")
    parser.add_argument("-b", "--build", action="store_true")
    parser.add_argument("-n", "--name", action="store_true")
    args = parser.parse_args()


    if args.pack:

        # Pack Engine for release
        engine = Engine(nowindow=True)
        engine.builder.pack_release()

    elif args.build:
            
        # Build game to EXE
        engine = Engine(nowindow=True)
        engine.builder.setup_game()
        engine.builder.create_exe()

    elif args.name: 

        # Setup new Project with name
        engine = Engine()
        engine.builder.setup_game(args.name)
        
    else:

        # Setup new no name Project 
        engine = Engine()
        engine.builder.setup_game()