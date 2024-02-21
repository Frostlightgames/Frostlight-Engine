import os
import sys
import glob
import datetime

class Logger:
    def __init__(self,engine,delete_old_logs:bool=False) -> None:

        """
        Initialise the engines logging system.

        The logging system helps to log important information and collects error messages.

        Args:
        
        - engine (Engine): The engine to access specific variables.
        - delete_old_logs (bool)=False: If true there will only be the newest logfile.

        !!!This is only used internally by the engine and should not be called in a game!!!
        """

        # Engine variable
        self.engine = engine

        # Setting starting variables
        self.logpath = os.path.join("logs",f"{datetime.datetime.now().strftime('%d.%m.%y %H-%M-%S')}.log")
        self.last_logged_second = 0
        self.last_logged_message = ""
        self.repeat_log_times = 1
        self.time_format = "%d.%m.%y %H:%M:%S:%f"

        if self.engine.logging:
            # Trying to create logfile
            try:

                # Create empty file
                if not os.path.exists(self.logpath):
                    if not os.path.exists("logs"):
                        os.mkdir("logs")
                    if delete_old_logs:
                        for filename in glob.glob("logs/*.log"):
                            os.remove(filename)
                    with open(self.logpath,"+w") as file:
                        file.write("")
            except Exception as e:

                # Creating logfile failed, printing instead
                print(f"[Engine {datetime.datetime.now().strftime(self.time_format)[:-4]}]: Could not create logfile ({e})")

    # Different log variants
    def error(self,message:str):

        """
        Logs an error.

        Args:

        - message (str): Content to log.

        Mostly used by the engine internally but can also be used for logging other error messages

        Example:
        ```
        self.logger.error("The Exception")
        ```
        """

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        self._log("Error",f"{message} in [{fname} line: {exc_tb.tb_lineno}]")

    def warning(self,message:str):

        """
        Logs a warning.

        Args:

        - message (str): Content to log.

        Example:
        ```
        self.logger.warning("Memory almost 80% filled!")
        ```
        """

        self._log("Warning",str(message))

    def info(self,message:str):

        """
        Logs an info.

        Args:

        - message (str): Content to log.

        Example:
        ```
        self.logger.info("I am a duck)
        ```
        """

        self._log("Info",str(message))

    def _log(self,prefix:str,message:str):

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
                if self.last_logged_message == message:

                    # Message is repeating
                    if self.last_logged_second != datetime.datetime.now().second:
                        self.last_logged_second = datetime.datetime.now().second

                        # Writing to logfile: caller + time + repeating count + log type + message
                        with open(self.logpath,"+at") as file:
                            self.repeat_log_times += 1
                            file.write(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix} x{self.repeat_log_times} | {message}\n")
                else:

                    # Storing last message and timestamp
                    self.last_logged_second = datetime.datetime.now().second
                    self.last_logged_message = message
                    self.repeat_log_times = 1

                    # Writing to logfile: caller + time + log type + message
                    with open(self.logpath,"+at") as file:
                        file.write(f"[{caller} {datetime.datetime.now().strftime(self.time_format)[:-4]}]: {prefix} | {message}\n")
            except Exception as e:
                print(f"[Engine {datetime.datetime.now().strftime(self.file_name_option)[:-4]}]: Could not log message ({message}) | ({e})")