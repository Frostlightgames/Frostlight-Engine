from __init__ import *

from core.log_manager import *
from core.window import *

class Core:
    def __init__(self,args={},*loop_functions):
        self.main_loop_running = True
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.last_time = time.time()
        self.fps_limit = args["fps_limit"]

        self.loop_functions = loop_functions

        self.build_manager = None
        self.event_manager = None
        self.input_manager = None
        self.logger = Logger()
        self.save_manager = None

        self.logger.info("Started Frostlightengine version 2.0.0")

    def get_fps(self) -> int:
        return int(min(self.clock.get_fps(),99999999))

    def start_main_loop(self) -> None:
        pygame.event.set_allowed([pygame.QUIT,
                                  pygame.WINDOWMOVED, pygame.VIDEORESIZE,
                                  pygame.KEYDOWN, pygame.KEYUP,
                                  pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION,
                                  pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN, pygame.JOYAXISMOTION, pygame.JOYHATMOTION,
                                  pygame.JOYDEVICEADDED, pygame.JOYDEVICEREMOVED])
        
        while self.main_loop_running:
            try:
                self.clock.tick(self.fps_limit)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.main_loop_running = False
                        self.logger.info("Closed window, stopping game.")

                self.delta_time = time.time() - self.last_time
                self.last_time = time.time()

                for function in self.loop_functions:
                    function()
            except:
                self.logger.error("Error while running main loop.")