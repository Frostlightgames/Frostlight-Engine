import inspect

from init import *

from core.core import Core as _Core
from core.window import Window
from core.sprite import Sprite
from core.input_manager import KEYBOARD,MOUSE,PRESSED,CLICKED,RELEASED

class FrostlightEngine:
    def __init__(self, window_size=[1920,1080], canvas_size=[1920,1080], window_mode=glfw.RESIZABLE, title="New Game", fps_limit=0):
        frame = inspect.currentframe()
        if frame is not None:
            args = inspect.getargvalues(frame)[3]
        else:
            args = {}
        self.__core = _Core(args, self.__engine_update, self.update, self.draw, self.__engine_draw)
        self.__core.event_window_resize = self.__window_resize
        self.__core.event_quit = self.event_quit

        self.window = Window(window_size,canvas_size)
        GLOBAL_ENVIRONMENT.MODERNGL_CONTEXT = self.window._ctx
        
        self.logger = self.__core.logger
        self.save_manager = self.__core.save_manager
        self.input = self.__core.input_manager
        self.input._register_callbacks(self.window.window)
        self.delta_time = self.__core.delta_time

    def __engine_update(self):
        self.input._update()
        self.window.poll_events()

        if self.window.should_close():
            self.event_quit()
            self.__core.main_loop_running = False
            self.window.close()
             
        self.delta_time = self.__core.delta_time

    def update(self):
        ...

    def draw(self):
        ...
    
    def __engine_draw(self):
        self.window.update()

    def event_quit(self):
        ...

    def __window_resize(self,window_size):
        self.window.resize(window_size)

    def run(self):
        self.__core.start_main_loop()

if __name__ == "__main__":
    engine = FrostlightEngine()