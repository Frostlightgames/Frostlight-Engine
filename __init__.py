import os
import time
import pygame
import random
import inspect

class Env:
    def __init__(self) -> None:
        self.engine = None
        self.values = {}

ENV = Env()

from _core.window import WINDOWED,FULLSCREEN,WINDOWED_FULLSCREEN,FRAMELESS,FIXED,HIDDEN,KEEP,SCALE,FREE