import os
import sys
import time
import math
import numpy
import pygame
import moderngl
import datetime
import traceback

from PIL import Image
from pathlib import Path

pygame.init()

DATE_TIME_FORMAT = "%d.%m.%y %H-%M-%S"

class GlobalEnvironment:
    MODERNGL_CONTEXT = None

GLOBAL_ENVIRONMENT = GlobalEnvironment()