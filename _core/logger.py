import os
import sys
import glob
import datetime
import traceback
from multipledispatch import dispatch

class _LogType():
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

class Logger:
    def __init__(self,logging:bool=True,logging_only_once:bool=True) -> None:
        """
        Initialise the engines logging system.

        The logging system helps to log important information and collects error messages.

        Args:
        
        - engine (Engine): The engine to access specific variables.
        - delete_old_logs (bool)=False: If true there will only be the newest logfile.

        !!!This is only used internally by the engine and should not be called in a game!!!
        """

        # Setting starting variables
        self.logging = True
        self.logpath = os.path.join("logs",f"{datetime.datetime.now().strftime('%d.%m.%y %H-%M-%S')}.log")
        self.last_logged_second = 0
        self.last_logged_message = ""
        self.last_logged_type = ""
        self.last_logged_pos = 0
        self.repeat_log_times = 1
        self.max_prefix_length = 7
        self.file_size = 0
        self.time_format = "%d.%m.%y %H:%M:%S:%f"
        self.INFO = _LogType(0)
        self.WARNING = _LogType(1)
        self.ERROR = _LogType(2)

        if self.logging:
            # Trying to create logfile
            try:

                # Create empty file
                if not os.path.exists(self.logpath):
                    if not os.path.exists("logs"):
                        os.mkdir("logs")
                    if logging_only_once:
                        for filename in glob.glob("logs/*.log"):
                            os.remove(filename)
                    with open(self.logpath,"+w") as file:
                        file.write("")
            except Exception as e:

                # Creating logfile failed, printing instead
                print(f"[Engine {datetime.datetime.now().strftime(self.time_format)[:-4]}]: Could not create logfile ({e})")

    @dispatch()
    def swich_logging(self):
        """
        The logging status of the Logger is swiched.

        Examples:
        ```
        self.swich_logging()
        """
        self.logging = not self.logging

    @dispatch(bool)
    def swich_logging(self,logging:bool):
        """
        The logging status of the Logger will be set to the value of the logging variable.

        Args:
        - logging (bool): False deaktivates the logging. True aktivates the logging.

        Examples:
        ```
        self.swich_logging(False)
        ```
        """
        self.logging = logging

    @dispatch(str)
    def log(self,message:str):
        """
        Logs a message.

        Args:

        - message (str): Content to log.

        Examples:
        ```
        self.log("Programm is working fine!")
        ```
        """
        self._log("Log",message,"\x1b[1;34;40m")

    @dispatch(_LogType,str)
    def log(self,LogType:_LogType,message:str):
        """
        Logs a message with a Prefix.

        Args:
        
        - type_or_msg (LogType | str): Type of log.
        - message (str): Content to log.

        Examples:
        ```
        self.log(INFO,"Programm is working fine!")
        self.log(WARNING,"Memory almost 80% filled!")
        self.log(ERROR,"XY not found!")
        ```
        """
        self._log(LogType.prefix,message,LogType.color)
    
    @dispatch()
    def log(self):
        """
        Logs an Exeption.

        Args:
        
        - type_or_msg (LogType | str): Type of log or just a message.
        - message (str): Content to log. Only when a type is given!

        Examples:
        ```
        try:
            ...
        exept:
            self.log()
        ```
        """
        t = traceback.format_exc().split("\n")
        msg = t[-2]
        tb = ""
        for i in range(1,len(t)-2):
            tb += t[i]+"\n"
        tb[:-1]
        self._log("Error",msg,"\x1b[1;31;40m",tb)

    def _log(self,prefix:str,message:str,prefix_color="",tb=""):

        """
        Writes logged content to file.

        Args:

        - prefix (str): Importance of content 
        - message (str): Content to write to logfile.
        - prefix_color (str): Color code for Prefix in the commandline.
        - tb (str): Traceback of an Error.

        !!!This is only used internally by the engine and should not be called in a game!!!
        """

        if self.logging:
            caller = "Engine"
            try:
                if self.last_logged_message == message and self.last_logged_type == prefix:

                    # Message is repeating

                    # if self.last_logged_second <= datetime.datetime.now().second:
                    #     self.last_logged_second = datetime.datetime.now().second

                    # Writing to logfile: caller + time + repeating count + log type + message
                    try:
                        with open(self.logpath,"r+") as file:
                            file.seek(self.last_logged_pos,0)
                            file.truncate()
                
                        with open(self.logpath,"a+") as file:
                            self.repeat_log_times += 1
                            
                            if tb == "":
                                file.write(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix.center(self.max_prefix_length)} | {message} | x{self.repeat_log_times}\n")
                                print('\033[1A', end='\x1b[2K')
                                print(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix_color+prefix.center(self.max_prefix_length)}\x1b[0m | {message} | x{self.repeat_log_times}")
                            else:
                                tbc = tb.count("\n")+3
                                for i in range(tbc):
                                    print('\033[1A', end='\x1b[2K')
                                file.write(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix.center(self.max_prefix_length)} | {message} | x{self.repeat_log_times}\n\n")
                                file.write(tb+"\n")
                                print(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix_color+prefix.center(self.max_prefix_length)}\x1b[0m | {message} | x{self.repeat_log_times}\n")
                                print(tb)
                    except KeyboardInterrupt:
                        exit(0)
                        
                else:
                    # Storing last message and timestampd
                    self.last_logged_second = datetime.datetime.now().second
                    self.last_logged_message = message
                    self.last_logged_type = prefix
                    self.repeat_log_times = 1
                    self.file_size += 1

                    # Writing to logfile: caller + time + log type + message
                    with open(self.logpath,"+at") as file:
                        self.last_logged_pos = file.tell()
                        if tb != "":
                            message += "\n"
                        file.write(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix.center(self.max_prefix_length)} | {message}\n")
                        print(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix_color+prefix.center(self.max_prefix_length)}\x1b[0m | {message}")
                        if tb != "":
                            file.write(tb+"\n")
                            print(tb)
            except Exception as e:
                print(f"[Engine {datetime.datetime.now().strftime(self.time_format)[:-4]}]: Could not log message ({message}) | ({e})")
            
