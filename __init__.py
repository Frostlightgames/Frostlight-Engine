class Env:
    def __init__(self) -> None:
        self.engine = None

ENV = Env()

from _core.logger import _LogType
from _core.window import WindowMode,AspectRatioMode

INFO = _LogType(0)
WARNING = _LogType(1)
ERROR = _LogType(2)

WINDOWED = WindowMode(0)
FULLSCREEN = WindowMode(1)
WINDOWED_FULLSCREEN = WindowMode(2)
FRAMELESS = WindowMode(3)
FIXED = WindowMode(4)
HIDDEN = WindowMode(5)

KEEP = AspectRatioMode(0)
SCALE = AspectRatioMode(1)
FREE = AspectRatioMode(2)