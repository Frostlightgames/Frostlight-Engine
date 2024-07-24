from _core.logger import Logger
from _core.save_manager import SaveManager
class Core:
    def __init__(self,
            debug:bool=False,
            fps_limit:int=0,
            logging:bool=True,
            logging_only_once=True,
            mouse_visible:bool=True,
            vsync:bool=False,
            window_centered:bool=True,
            window_color_depth:int=16,
            window_fullscreen:bool=False,
            window_icon_path:str="",
            window_name:str="New Game",
            window_resizable:bool=True,
            window_size:list=None,
            save_manager_path="data/saves/save") -> None:
        
        self.logger = Logger(logging,logging_only_once)
        self.save_manager = SaveManager(self.logger,save_manager_path)

    def loop(self,update_func,draw_func):
        while True:
            update_func()
            draw_func()