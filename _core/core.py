import pygame

from _core.logger import Logger
from _core.builder import Builder
from _core.save_manager import SaveManager
from _core.window import Window,WINDOWED,KEEP
class Core:
    def __init__(self,
            debug:bool=False,
            fps_limit:int=0,
            game_language:str="en",
            game_version:str="1.0",
            logging:bool=True,
            logging_only_once=True,
            window_mode=WINDOWED,
            aspect_mode=KEEP,
            window_size=None,
            centered=True,
            mouse_visible=True,
            window_name="",
            icon_path="",
            position=[0,0],
            color_depth=16,
            vsync = True,
            save_manager_path="data/saves/save") -> None:
        
        self.logger = Logger(logging,logging_only_once)
        self.save_manager = SaveManager(self.logger,save_manager_path)
        self.builder = Builder(self.logger)
        
        self.window = Window(window_mode,aspect_mode,window_size,centered,mouse_visible,window_name,icon_path,position,color_depth,vsync)

    def loop(self,*functions):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

            for function in functions:
                function()

            self.window.update()