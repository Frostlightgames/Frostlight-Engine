import pygame

from __init__ import ENV

from _core.builder import Builder
from _core.event_manager import EventManager
from _core.input_manager import InputManager
from _core.logger import Logger
from _core.save_manager import SaveManager
from _core.window import Window

def event_event(event):

    # Event function to overwrite on event
    """
    This function can be overwritten to react to every engine event.
    Event is called after the engine event.

    Args:

    - event: Data about the event.

    Example:
    ```
    def event_event(event):
        print(f"Engine event occurred: {event}")
    ```
    """

def event_error(exception:Exception):
    pass

def event_quit():

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

def event_window_move(position:list[int,int]):

    # Event function to overwrite on window move
    """
    This function can be overwritten to react to the window move event.
    Event is called after the window moved.

    Args:

    - position (list[int,int]): Monitor position to where to window moved.

    Example:
    ```
    def event_window_move(position:list[int,int]):
        print(f"The window moved to: {position}")
    ```
    """

def event_window_resize(size:list[int,int]):

    # Event function to overwrite on window resize
    """
    This function can be overwritten to react to the window resize event.
    Event is called after the window is resized.

    Args:

    - size (list[int,int]): New window size.

    Example:
    ```
    def event_window_resize(size:list[int,int]):
        print(f"The window was resized to: {size}")
    ```
    """

def event_window_mode_changed(new_mode:str):

    # Event function to overwrite on window mode changed
    """
    This function can be overwritten to react to the mode change of the window.
    Event is called after the mode changed.

    Args:

    - new_mode (str): The window mode after the event

    Example:
    ```
    def event_window_mode_changed(new_mode:str):
        print(f"The window mode changed to: {new_mode}")
    ```
    """

def event_window_changed(event):

    # Event function to overwrite on window changed
    """
    This function can be overwritten to react to a change of the window.
    Event is called after the change.

    Args:

    - event: Data about the event.

    Example:
    ```
    def event_window_changed(event):
        print(f"The window changed: {event}")
    ```
    """

def event_keydown(key:int,unicode:str):

    # Event function to overwrite on keypress
    """
    This function can be overwritten to react to the keypress event.
    Event is called after a key is pressed.

    Args:

    - key (int): Index of pressed key.
    - unicode (str): Displayable unicode of key.

    Example:
    ```
    def event_keydown(key:int,unicode:str):
        print(f"Key {unicode} with id {key} was pressed")
    ```
    """

def event_keyup(key:int,unicode:str):

    # Event function to overwrite on key release
    """
    This function can be overwritten to react to the key release event.
    Event is called after a key is released.

    Args:
    
    - key (int): Index of released key.
    - unicode (str): Displayable unicode of key.

    Example:
    ```
    def event_keyup(key:int,unicode:str):
        print(f"Key {unicode} with id {key} was released")
    ```
    """

def event_mouse_buttondown(button:int,position:list[int,int]):

    # Event function to overwrite on mouse click
    """
    This function can be overwritten to react to a mouse click.
    Event is called after the mouse is clicked.

    Args:

    - button (int): Index of clicked button.
    - position (list[int,int]): Position the mouse was on when clicked.

    Example:
    ```
    def event_mouse_buttondown(button:int,position:list[int,int]):
        print(f"Mouse button {button} was pressed at position {position}}")
    ```
    """

def event_mouse_buttonup(button:int,position:list[int,int]):

    # Event function to overwrite on mouse release
    """
    This function can be overwritten to react to a mouse button release.
    Event is called after the mouse button is released.

    Args:

    - button (int): Index of released button.
    - position (list[int,int]): Position the mouse was on when released.

    Example:
    ```
    def event_mouse_buttonup(button:int,position:list[int,int]):
        print(f"Mouse button {button} was released at position {position}}")
    ```
    """

def event_joystick_buttondown(button:int,joystick_id:int,instance_id:int):

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
    def event_joystick_buttondown(button:int,joystick_id:int,instance_id:int):
        print(f"Button {button} was pressed at joystick {joystick_id}")
    ```
    """

def event_joystick_buttonup(button:int,joystick_id:int,instance_id:int):
    
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
    def event_joystick_buttonup(button:int,joystick_id:int,instance_id:int):
        print(f"Button {button} was released at joystick {joystick_id}")
    ```
    """

def event_joystick_axismotion(joystick_id:int,instance_id:int,axis:int,value:float):
    
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
    def event_joystick_axismotion(joystick_id:int,instance_id:int,axis:int,value:int):
        print(f"Axis {axis} detected motion {value} at joystick {joystick_id}")
    ```
    """

def event_joystick_hatmotion(joystick_id:int,instance_id:int,hat:int,value:int):
    
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
    def event_joystick_hatmotion(joystick_id:int,instance_id:int,hat:int,value:int):
        print(f"Hat {hat} detected motion {value} at joystick {joy_id}")
    ```
    """

def event_joystick_added(device_index:int,guid:str):
    
    # Event function to overwrite on joystick connected
    """
    This function can be overwritten to react to a new joystick device registered.
    Event is called after the joystick is added.

    Args:

    - device_index (int): Index id of joystick object.
    - guid (int): Gamepad unique id.

    Example:
    ```
    def event_joystick_added(device_index:int,guid:str):
        print(f"Connected new joystick {guid} at {device_index}")
    ```
    """

def event_joystick_removed(instance_id:int):
    
    # Event function to overwrite on joystick disconnected
    """
    This function can be overwritten to react to the removal of a registered joystick device.
    Event is called after the joystick is removed.

    Args:

    - instance_id (int): Instance id of joystick object.

    Example:
    ```
    def event_joystick_removed(instance_id:int):
        print(f"Joystick {instance_id} disconnected!!!")
    ```
    """

class Core:
    def __init__(self,debug:bool=False) -> None:
        self.clock = pygame.time.Clock()
        self.builder = None
        self.event_manager = None
        self.input_manager = None
        self.logger = None
        self.save_manager = None
        self.window = None

    def init_core(self):
        self.logger = Logger(logging=ENV.values["logging"],logging_only_once=ENV.values["logging_only_once"])
        self.builder = Builder(logger=self.logger)
        self.event_manager = EventManager(logger=self.logger)
        self.input_manager = InputManager(logger=self.logger)
        self.save_manager = SaveManager(logger=self.logger,path=ENV.values["save_manager_path"])
        self.window = Window(window_mode=ENV.values["window_mode"],aspect_mode=ENV.values["window_aspect_mode"],window_size=ENV.values["window_size"],
                             centered=ENV.values["window_centered"],mouse_visible=ENV.values["mouse_visible"],window_name=ENV.values["window_name"],
                             icon_path=ENV.values["window_icon_path"],position=ENV.values["window_position"],color_depth=ENV.values["window_color_depth"],
                             vsync=ENV.values["vsync"])
        
    def loop(self,*functions):
        pygame.event.set_allowed([pygame.QUIT, pygame.WINDOWMOVED, pygame.VIDEORESIZE, pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN,
                                  pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN, pygame.JOYAXISMOTION, 
                                  pygame.JOYHATMOTION, pygame.JOYDEVICEADDED, pygame.JOYDEVICEREMOVED])
        while True:
            self.clock.tick(ENV.values["fps_limit"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    event_quit()
                    exit(0)

            for function in functions:
                function()

            self.window.update()