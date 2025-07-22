import os
import sys
import time
import numpy
import pygame
import inspect
import moderngl
import datetime
import traceback

from PIL import Image
from pathlib import Path

pygame.init()

DATE_TIME_FORMAT = "%d.%m.%y %H-%M-%S"
WINDOW_CONTEXT = None