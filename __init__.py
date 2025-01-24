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
from _core.core import event_quit
from _core.event_manager import EventManager

event_event = EventManager.event_event

def event_event():
    pass