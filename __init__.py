import os
import time
import pygame
import random

class Env:
    def __init__(self) -> None:
        self.engine = None

ENV = Env()

from _core import WINDOWED,FULLSCREEN,WINDOWED_FULLSCREEN,FRAMELESS,FIXED,HIDDEN,KEEP,SCALE,FREE