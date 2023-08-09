import os
import datetime

class Logger:
    def __init__(self) -> None:
        self.logpath = os.path.join("data","log.txt")
        self.last_logged_second = 0
        self.last_logged_message = ""
        self.repeat_log_times = 1
        try:
            if not os.path.exists(os.path.join("data","log.txt")):
                with open(self.logpath,"+w") as file:
                    file.write("")
                
        except Exception as e:
            print(f"[Engine {datetime.datetime.now()()}]: Could not create logfile ({e})")

    def error(self,message:str):
        self.__log__("Error",str(message))

    def warning(self,message:str):
        self.__log__("Warning",str(message))

    def info(self,message:str):
        self.__log__("Info",str(message))

    def __log__(self,prefix:str,message:str):
        caller = "Engin"

        try:
            if self.last_logged_message == message:
                if self.last_logged_second != datetime.datetime.now().second:
                    self.last_logged_second = datetime.datetime.now().second
                    with open(self.logpath,"+at") as file:
                        self.repeat_log_times += 1
                        file.write(f"[{caller} {datetime.datetime.now()} x{self.repeat_log_times}]: {prefix} | {message}\n")
            else:
                self.last_logged_second = datetime.datetime.now().second
                self.last_logged_message = message
                self.repeat_log_times = 1
                with open(self.logpath,"+at") as file:
                    file.write(f"[{caller} {datetime.datetime.now()}]: {prefix} | {message}\n")
        except Exception as e:
            print(f"[Engine {datetime.datetime.now()}]: Could not log message ({message}) | ({e})")

    def clear(self):
        try:
            if not os.path.exists(os.path.join("data","log.txt")):
                with open(self.logpath,"+w") as file:
                    file.write("")
                    file.close()
                
        except Exception as e:
            print(f"[Engine {datetime.datetime.now()}]: Could not clear logfile ({e})")