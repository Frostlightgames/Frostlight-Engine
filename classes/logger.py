import os
import sys
import datetime

class Logger:
    def __init__(self,engine,delete_old_logs:bool=False) -> None:

        # Engine variable
        self.engine = engine

        # Setting starting variables
        self.logpath = os.path.join("logs",f"{datetime.datetime.now().strftime('%d-%m-%y %H-%M-%S')}.log")
        self.last_logged_second = 0
        self.last_logged_message = ""
        self.repeat_log_times = 1
        self.time_format = "%d-%m-%y %H:%M:%S:%f"

        # Trying to create logfile
        try:

            # Create empty file
            if not os.path.exists(self.logpath) or delete_old_logs:
                if not os.path.exists("logs"):
                    os.mkdir("logs")
                with open(self.logpath,"+w") as file:
                    file.write("")
        except Exception as e:

            # Creating logfile failed, printing instead
            print(f"[Engine {datetime.datetime.now().strftime(self.time_format)[:-4]}]: Could not create logfile ({e})")

    # Different log variants
    def error(self,message:str):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        self.__log__("Error",f"{message} in [{fname} line: {exc_tb.tb_lineno}]")

    def warning(self,message:str):
        self.__log__("Warning",str(message))

    def info(self,message:str):
        self.__log__("Info",str(message))

    def __log__(self,prefix:str,message:str):
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