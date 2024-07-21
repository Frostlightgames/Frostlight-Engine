import os
import sys
import glob
import datetime

from __init__ import ENV,LogType



class Logger:
    def __init__(self,logging_only_once:bool=True) -> None:

        """
        Initialise the engines logging system.

        The logging system helps to log important information and collects error messages.

        Args:
        
        - engine (Engine): The engine to access specific variables.
        - delete_old_logs (bool)=False: If true there will only be the newest logfile.

        !!!This is only used internally by the engine and should not be called in a game!!!
        """

        # Engine variable
        self.engine = ENV.engine

        # Setting starting variables
        self.logpath = os.path.join("logs",f"{datetime.datetime.now().strftime('%d.%m.%y %H-%M-%S')}.log")
        self.last_logged_second = 0
        self.last_logged_message = ""
        self.last_logged_type = ""
        self.repeat_log_times = 1
        self.time_format = "%d.%m.%y %H:%M:%S:%f"

        if self.engine.logging:
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

    def log(self,type_or_msg:LogType | str,message:str=None):
        """
        Logs a message. If type is set then the message has a prefix.

        Args:
        
        - type_or_msg (LogType | str): Type of log or just a message.
        - message (str): Content to log. Only when a type is given!

        Examples:
        ```
        self.logger.log("Programm is working fine!")
        self.logger.log(INFO,"Programm is working fine!")
        self.logger.log(WARNING,"Memory almost 80% filled!")
        self.logger.log(ERROR,"Exception")
        ```
        """
        if type(type_or_msg) == str:
            self._log("Log",type_or_msg,"\x1b[1;37;40m")
        else:
            if type_or_msg.type == 2:
            
                exc_type, exc_obj, exc_tb = sys.exc_info()
                if exc_tb != None:
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    message = f"{message} in [{fname} line: {exc_tb.tb_lineno}]"
                else:
                    self._log(type_or_msg.prefix,message,type_or_msg.color)
            else:
                self._log(type_or_msg.prefix,message,type_or_msg.color)


    def _log(self,prefix:str,message:str,prefix_color=""):

        """
        Writes logged content to file.

        Args:

        - prefix (str): Importance of content 
        - message (str): Content to write to logfile.

        !!!This is only used internally by the engine and should not be called in a game!!!
        """

        if self.engine.logging:
            caller = "Engine"
            try:
                if self.last_logged_message == message and self.last_logged_type == prefix:

                    # Message is repeating

                    if self.last_logged_second <= datetime.datetime.now().second:
                        self.last_logged_second = datetime.datetime.now().second

                        # Writing to logfile: caller + time + repeating count + log type + message
                        with open(self.logpath,"+at") as file:
                            self.repeat_log_times += 1
                            file.write(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix} | x{self.repeat_log_times} | {message}\n")
                        print(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix_color+prefix}\x1b[0m | x{self.repeat_log_times} | {message}\n")
                else:
                    
                    # Storing last message and timestamp
                    self.last_logged_second = datetime.datetime.now().second
                    self.last_logged_message = message
                    self.last_logged_type = prefix
                    self.repeat_log_times = 1

                    # Writing to logfile: caller + time + log type + message
                    with open(self.logpath,"+at") as file:
                        file.write(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix} | {message}\n")
                    print(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix_color+prefix}\x1b[0m | {message}\n")
            except Exception as e:
                print(f"[Engine {datetime.datetime.now().strftime(self.file_name_option)[:-4]}]: Could not log message ({message}) | ({e})")
