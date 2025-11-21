from init import *

from core.builder import *
from core.log_manager import *
from core.window import *
from core.save_manager import *
from core.input_manager import *

class Core:
    def __init__(self,args={},*loop_functions):
        self.main_loop_running = True
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.last_time = time.time()
        self.fps_limit = args["fps_limit"]

        self.loop_functions = loop_functions

        self.build_manager = Builder()
        self.event_manager = None
        self.input_manager = InputManager()
        self.logger = Logger()
        self.save_manager = SaveManager(self.logger)

        self.event_window_resize = None
        self.event_quit = None

        self.logger.info("Started Frostlightengine version 2.0.0 [DEV]")

    def get_fps(self) -> int:
        return int(min(self.clock.get_fps(),99999999))

    def start_main_loop(self) -> None:        
        while self.main_loop_running:
            try:
                self.clock.tick(self.fps_limit)

                self.delta_time = time.time() - self.last_time
                self.last_time = time.time()

                for function in self.loop_functions:
                    function()
            except Exception as e:
                if type(Exception) == KeyboardInterrupt:
                    self.main_loop_running = False
                    self.event_quit()
                else:
                    self.logger.error("Error while running main loop.")
