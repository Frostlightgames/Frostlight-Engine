import pygame

from __init__ import ENV

from _core.logger import Logger
from _core.builder import Builder
from _core.save_manager import SaveManager
from _core.window import Window
class Core:
    def __init__(self,debug:bool=False) -> None:
        self.clock = pygame.time.Clock()
        self.builder = None
        self.logger = None
        self.save_manager = None
        self.window = None

    def init_core(self):
        self.logger = Logger(logging=ENV.values["logging"],logging_only_once=ENV.values["logging_only_once"])
        self.save_manager = SaveManager(logger=self.logger,path=ENV.values["save_manager_path"])
        self.builder = Builder(logger=self.logger)
        self.window = Window(window_mode=ENV.values["window_mode"],aspect_mode=ENV.values["window_aspect_mode"],window_size=ENV.values["window_size"],
                             centered=ENV.values["window_centered"],mouse_visible=ENV.values["mouse_visible"],window_name=ENV.values["window_name"],
                             icon_path=ENV.values["window_icon_path"],position=ENV.values["window_position"],color_depth=ENV.values["window_color_depth"],
                             vsync=ENV.values["vsync"])
        
    def loop(self,*functions):
        while True:
            self.clock.tick(ENV.values["fps_limit"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

            for function in functions:
                function()

            self.window.update()