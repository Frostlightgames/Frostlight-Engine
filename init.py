import os
import sys
import time
import math
import glfw
import json
import numpy
import pygame
import moderngl
import datetime
import traceback

from PIL import Image
from pathlib import Path
from cryptography.fernet import Fernet

pygame.init()

DATE_TIME_FORMAT = "%d.%m.%y %H-%M-%S"

class GlobalEnvironment:
    MODERNGL_CONTEXT = None

GLOBAL_ENVIRONMENT = GlobalEnvironment()