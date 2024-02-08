import os
import time
import pygame
import argparse
from classes.save import *
from classes.input import *
from classes.logger import *
from classes.window import *
from classes.builder import *

class Engine:
    def __init__(self,
                 catch_error:bool=True,
                 color_depth:int=16,
                 delete_old_logs:bool=False,
                 fps:int=0,
                 fullscreen:bool=False,
                 game_version:str="1.0",
                 language:str="en",
                 logging:bool=True,
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
        self.catch_error = catch_error
        self.logging = logging
        self.run_game = True
        self.sounds = sounds

        # Integer and float variables go here
        self.fps = fps
        self.delta_time = 1
        self.last_time = time.time()
        self.version = 0.1

        # String variables go here
        self.engine_version = "1.1.0 [DEV]"
        self.game_state = "intro"
        self.game_version = game_version
        self.language = language

        # List variables go here
        self.display_update_rects = []

        # Object variables go here
        self.clock = pygame.time.Clock()
        self._builder = Builder(self)
        self.logger = Logger(self,delete_old_logs)
        self.input = Input(self)
        self.save_manager = SaveManager(self,os.path.join("data","saves","save"))
        self.window = Window(self,window_size,fullscreen,resizable,nowindow,window_centered,vsync,window_name,mouse_visible,color_depth)

        # Object processing go here
        self.window._create()
        pygame.event.set_allowed([pygame.QUIT,
                                  pygame.WINDOWMOVED, 
                                  pygame.VIDEORESIZE, 
                                  pygame.KEYDOWN,
                                  pygame.KEYUP,
                                  pygame.MOUSEBUTTONDOWN,
                                  pygame.MOUSEBUTTONUP, 
                                  pygame.JOYBUTTONUP, 
                                  pygame.JOYBUTTONDOWN, 
                                  pygame.JOYAXISMOTION, 
                                  pygame.JOYHATMOTION, 
                                  pygame.JOYDEVICEADDED, 
                                  pygame.JOYDEVICEREMOVED])

    def _get_events(self):
        self.clock.tick(self.fps)
        self.input._update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            # Window events
            elif event.type == pygame.WINDOWMOVED:
                self.last_time = time.time()
                self.delta_time = 0
                self.event_window_move([event.x,event.y])
                self.event_window_resize([event.w,event.h])

            elif event.type == pygame.VIDEORESIZE:
                if not self.window.fullscreen:
                    self.last_time = time.time()
                    self.delta_time = 0
                    self.window.resize([event.w,event.h])

            # Keyboard events
            elif event.type == pygame.KEYDOWN:
                self.input._handle_key_event(event)
                if event.key == pygame.K_F11:
                    self.window.toggle_fullscreen()
                self.event_keydown(event.key,event.unicode)

            elif event.type == pygame.KEYUP:
                self.input._handle_key_event(event)
                self.event_keyup(event.key,event.unicode)
                
            # Mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.input._handle_mouse_event(event)
                self.event_mouse_buttondown(event.button,event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.input._handle_mouse_event(event)
                self.event_mouse_buttonup(event.button,event.pos)

            # Joystick events
            elif event.type == pygame.JOYBUTTONDOWN:
                self.input._handle_joy_event(event)
                self.event_joystick_buttondown(event.button,event.joy,event.instance_id)

            elif event.type == pygame.JOYBUTTONUP:
                self.input._handle_joy_event(event)
                self.event_joystick_buttonup(event.button,event.joy,event.instance_id)

            elif event.type == pygame.JOYAXISMOTION:
                self.input._handle_joy_event(event)
                self.event_joystick_axismotion(event.joy,event.instance_id,event.axis,event.value)

            elif event.type == pygame.JOYHATMOTION:
                self.input._handle_joy_event(event)
                self.event_joystick_hatmotion(event.button)

            elif event.type == pygame.JOYDEVICEADDED:
                self.input._init_joysticks()
                self.event_joystick_added(event.device_index,event.guid)

            elif event.type == pygame.JOYDEVICEREMOVED:
                self.input._init_joysticks()
                self.event_joystick_removed(event.instance_id)

    def event_quit(self):
        pass

    def event_window_move(self,position:list[int,int]):
        pass

    def event_window_resize(self,size:list[int,int]):
        pass
    
    def event_keydown(self,key:int,unicode:str):
        pass
    
    def event_keyup(self,key:int,unicode:str):
        pass

    def event_mouse_buttondown(sefl,button:int,position:list[int,int]):
        pass
    
    def event_mouse_buttonup(sefl,button:int,position:list[int,int]):
        pass
    
    def event_joystick_buttondown(sefl,button:int,joystick_id:int,instance_id:int):
        pass
    
    def event_joystick_buttonup(sefl,button:int,joystick_id:int,instance_id:int):
        pass
    
    def event_joystick_axismotion(sefl,joy_id:int,instance_id:int,axis:int,value:int):
        pass
    
    def event_joystick_hatmotion(self,hat:int,joystick_id:int,instance_id:int):
        pass
    
    def event_joystick_added(self,device_index:int,guid:str):
        pass
    
    def event_joystick_removed(self,instance_id:int):
        pass

    def _engine_update(self):

        # Update that runs before normal update
        self.delta_time = time.time()-self.last_time
        self.last_time = time.time()

    def _engine_draw(self):

        # Draw that runs after normal draw
        pygame.display.update()

    def run(self):

        # Starting game engine
        self.logger.info(f"Starting [Engine version {self.engine_version} | Game version {self.game_version}]")
        if self.catch_error:
            while self.run_game:

                # Main loop
                try:
                    self._get_events()
                    self._engine_update()
                    self.update()
                    self.draw()
                    self._engine_draw()
                except Exception as e:

                    # Error logging and catching
                    self.logger.error(e)
        else:
            while self.run_game:
                
                # Main loop
                self._get_events()
                self._engine_update()
                self.update()
                self.draw()
                self._engine_draw()
            
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
        engine._builder._pack_release()

    elif args.build:
    
        # Build game to EXE
        engine = Engine(nowindow=True)
        engine._builder._setup_game()
        engine._builder._create_exe()

    elif args.name: 

        # Setup new Project with name
        engine = Engine()
        engine._builder._setup_game(args.name)

    else:

        # Setup new no name Project 
        engine = Engine()
        engine._builder._setup_game()