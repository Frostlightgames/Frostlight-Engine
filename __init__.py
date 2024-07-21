class Env:
    def __init__(self) -> None:
        self.engine = None

ENV = Env()

class LogType():
    def __init__(self,typ:int,prefix="",color = "\x1b[0m") -> None:
        self.type = typ
        self.prefix = prefix
        self.color = color
        if self.type == 0:
            self.prefix = "Info"
            self.color = "\x1b[1;32;40m"
        elif self.type == 1:
            self.prefix = "Warning"
            self.color = "\x1b[1;33;40m"
        elif self.type == 2:
            self.prefix = "Error"
            self.color = "\x1b[1;31;40m"
    
INFO = LogType(0)
WARNING = LogType(1)
ERROR = LogType(2)
