from logger import *


class Core:
    def __init__(self) -> None:
        pass

    def loop(self,update_func,draw_func):
        while True:
            update_func()
            draw_func()