from __init__ import *

import _core
from _core import dispatch
from _core.logger import _LogType
import _nodes

class Engine:
    def __init__(self,
            debug:bool=False,
            fps_limit:int=0,
            game_language:str="en",
            game_version:str="1.0",
            logging:bool=True,
            logging_only_once=True,
            window_mode=WINDOWED,
            window_aspect_mode=KEEP,
            window_size=None,
            window_centered=True,
            mouse_visible=True,
            window_name="",
            window_icon_path="",
            window_position=[0,0],
            window_color_depth=16,
            vsync = True,
            save_manager_path="data/saves/save") -> None:
        
        if ENV.engine == None:
            ENV.engine = self
        
        self._core = _core.Core(
            debug,
            fps_limit,
            game_language,
            game_version,
            logging,
            logging_only_once,
            window_mode,
            window_aspect_mode,
            window_size,
            window_centered,
            mouse_visible,
            window_name,
            window_icon_path,
            window_position,
            window_color_depth,
            vsync,
            save_manager_path)

        self.window = self._core.window

        self.nodes = _nodes

        self.game_state = ""

    @dispatch(str)
    def log(self,message:str):
        self._core.logger.log(message)

    @dispatch(_LogType,Exception)
    def log(self,LogType:_core.logger._LogType,message:Exception):
        self._core.logger.log(LogType,message)

    @dispatch(_LogType,str)
    def log(self,LogType:_core.logger._LogType,message:str):
        self._core.logger.log(LogType,message)

    @dispatch()
    def log(self):
        self._core.logger.log()
    
    @dispatch()
    def swich_logging(self):
        self._core.logger.swich_logging()
    
    @dispatch(bool)
    def swich_logging(self,logging:bool):
        self._core.logger.swich_logging(logging)

    def save(self,key,value) -> bool:
        self._core.save_manager.save(key,value)

    def load(self,key,default=None) -> any:
        self._core.save_manager.load(key,default)

    def backup(self,backup_path:str="data/saves/backup"):
        self._core.save_manager.backup(backup_path)

    def update(self):
        pass

    def draw(self):
        pass

    def test(self):
        # TODO
        # sys log mit infos über engine z.b. engine_version, game_version 
        print("Test")

    def run(self):
        self._core.loop(self.update,self.draw)