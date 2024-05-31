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

        # String variables go here
        self.engine_version = "1.1.1 [DEV]"
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

            elif event.type == pygame.VIDEORESIZE:
                if not self.window.fullscreen:
                    self.last_time = time.time()
                    self.delta_time = 0
                    self.window.resize([event.w,event.h])
                    self.event_window_resize([event.w,event.h])

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

        # Event function to overwrite on quit
        """
        This function can be overwritten to react to the game quit event.
        Event is called before the game closes.

        Args:

        - No args are required.

        Example:
        ```
        def event_quit(self):
            print("game end")
        ```
        """

    def event_window_move(self,position:list[int,int]):

        # Event function to overwrite on window move
        """
        This function can be overwritten to react to the window move event.
        Event is called after the window moved.

        Args:

        - position (list[int,int]): Monitor position to where to window moved.

        Example:
        ```
        def event_window_move(self,position:list[int,int]):
            print(f"The window moved to: {position}")
        ```
        """

    def event_window_resize(self,size:list[int,int]):

        # Event function to overwrite on window resize
        """
        This function can be overwritten to react to the window resize event.
        Event is called after the window is resized.

        Args:

        - size (list[int,int]): New window size.

        Example:
        ```
        def event_window_resize(self,size:list[int,int]):
            print(f"The window was resized to: {size}")
        ```
        """

    def event_keydown(self,key:int,unicode:str):

        # Event function to overwrite on keypress
        """
        This function can be overwritten to react to the keypress event.
        Event is called after a key is pressed.

        Args:

        - key (int): Index of pressed key.
        - unicode (str): Displayable unicode of key.

        Example:
        ```
        def event_keydown(self,key:int,unicode:str):
            print(f"Key {unicode} with id {key} was pressed")
        ```
        """

    def event_keyup(self,key:int,unicode:str):

        # Event function to overwrite on key release
        """
        This function can be overwritten to react to the key release event.
        Event is called after a key is released.

        Args:
        
        - key (int): Index of released key.
        - unicode (str): Displayable unicode of key.

        Example:
        ```
        def event_keyup(self,key:int,unicode:str):
            print(f"Key {unicode} with id {key} was released")
        ```
        """

    def event_mouse_buttondown(sefl,button:int,position:list[int,int]):

        # Event function to overwrite on mouse click
        """
        This function can be overwritten to react to a mouse click.
        Event is called after the mouse is clicked.

        Args:

        - button (int): Index of clicked button.
        - position (list[int,int]): Position the mouse was on when clicked.

        Example:
        ```
        def event_mouse_buttondown(sefl,button:int,position:list[int,int]):
            print(f"Mouse button {button} was pressed at position {position}}")
        ```
        """

    def event_mouse_buttonup(sefl,button:int,position:list[int,int]):

        # Event function to overwrite on mouse release
        """
        This function can be overwritten to react to a mouse button release.
        Event is called after the mouse button is released.

        Args:

        - button (int): Index of released button.
        - position (list[int,int]): Position the mouse was on when released.

        Example:
        ```
        def event_mouse_buttonup(sefl,button:int,position:list[int,int]):
            print(f"Mouse button {button} was released at position {position}}")
        ```
        """

    def event_joystick_buttondown(sefl,button:int,joystick_id:int,instance_id:int):

        # Event function to overwrite on joystick button click
        """
        This function can be overwritten to react to a joystick button press.
        Event is called after the joystick button press.

        Args:

        - button (int): Index of released button.
        - joystick_id (int): Index id of joystick object.
        - instance_id (int): Instance id of joystick object.

        Example:
        ```
        def event_joystick_buttondown(sefl,button:int,joystick_id:int,instance_id:int):
            print(f"Button {button} was pressed at joystick {joystick_id}")
        ```
        """

    def event_joystick_buttonup(sefl,button:int,joystick_id:int,instance_id:int):
        
        # Event function to overwrite on joystick button release
        """
        This function can be overwritten to react to a joystick button release.
        Event is called after the joystick button is released.

        Args:

        - button (int): Index of released button.
        - joystick_id (int): Index id of joystick object.
        - instance_id (int): Instance id of joystick object.

        Example:
        ```
        def event_joystick_buttonup(sefl,button:int,joystick_id:int,instance_id:int):
            print(f"Button {button} was released at joystick {joystick_id}")
        ```
        """
    
    def event_joystick_axismotion(sefl,joystick_id:int,instance_id:int,axis:int,value:float):
        
        # Event function to overwrite on joystick axis motion
        """
        This function can be overwritten to react to a joysticks axis motion.
        Event is called after the joystick axis motion.

        Args:

        - joystick_id (int): Index id of joystick object.
        - instance_id (int): Instance id of joystick object.
        - axis (int): Index of moved joystick axis.
        - value (float): Value of motion between -1.0 and 1.0.

        Example:
        ```
        def event_joystick_axismotion(sefl,joystick_id:int,instance_id:int,axis:int,value:int):
            print(f"Axis {axis} detected motion {value} at joystick {joystick_id}")
        ```
        """
    
    def event_joystick_hatmotion(self,joystick_id:int,instance_id:int,hat:int,value:int):
        
        # Event function to overwrite on joystick hat motion
        """
        This function can be overwritten to react to a joysticks hat motion.
        Event is called after the joystick hat motion.

        Args:

        - joystick_id (int): Index id of joystick object.
        - instance_id (int): Instance id of joystick object.
        - hat (int): Index of joystick hat.
        - value (int): Value of hat pressed: -1 or 0 or 1

        Example:
        ```
        def event_joystick_hatmotion(self,joystick_id:int,instance_id:int,hat:int,value:int):
            print(f"Hat {hat} detected motion {value} at joystick {joy_id}")
        ```
        """
    
    def event_joystick_added(self,device_index:int,guid:str):
        
        # Event function to overwrite on joystick connected
        """
        This function can be overwritten to react to a new joystick device registered.
        Event is called after the joystick is added.

        Args:

        - device_index (int): Index id of joystick object.
        - guid (int): Gamepad unique id.

        Example:
        ```
        def event_joystick_added(self,device_index:int,guid:str):
            print(f"Connected new joystick {guid} at {device_index}")
        ```
        """
    
    def event_joystick_removed(self,instance_id:int):
        
        # Event function to overwrite on joystick disconnected
        """
        This function can be overwritten to react to the removal of a registered joystick device.
        Event is called after the joystick is removed.

        Args:

        - instance_id (int): Instance id of joystick object.

        Example:
        ```
        def event_joystick_removed(self,instance_id:int):
            print(f"Joystick {instance_id} disconnected!!!")
        ```
        """

    def _engine_update(self):

        # Update that runs before normal update
        self.delta_time = time.time()-self.last_time
        self.last_time = time.time()

    def _engine_draw(self):

        # Draw that runs after normal draw
        pygame.display.update()

    def run(self):

        """
        This function starts the main game loop

        Args:

        - No args are required.

        Example:
        ```
        if __name__ == "__main__"
            game = Game()
            game.run()
        ```
        """

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

        """
        This function closes the game loop

        Args:

        - No args are required.

        Example:
        ```
        i = 0
        while True:
            i += 1
            if i == 10:
                self.quit()
        ```
        """
        # trigger quit event
        self.event_quit()
        
        # Quit game loop
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
        engine = Engine(nowindow=True)
        engine._builder._setup_game(args.name)

    else:

        # Setup new no name Project
        engine = Engine(nowindow=True)
        engine._builder._setup_game()