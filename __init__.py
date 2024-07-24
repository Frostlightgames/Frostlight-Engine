class Env:
    def __init__(self) -> None:
        self.engine = None

ENV = Env()

from _core.logger import _LogType

INFO = _LogType(0)
WARNING = _LogType(1)
ERROR = _LogType(2)