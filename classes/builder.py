import os

class Builder:
    def __init__(self,engine) -> None:

        # Engine variable
        self.engine = engine

    def setup_game(self,name:str="New Game"):

        # Create engine tree
        directories_created = 0
        files_created = 0
        directories_to_create = ["data","screenshots",os.path.join("data","classes"),os.path.join("data","saves"),os.path.join("data","sprites")]
        
        # Creating directories
        for directory in directories_to_create:
            try:
                os.mkdir(directory)
                directories_created += 1
            except FileExistsError:
                self.engine.logger.warning(f"Skipping creation of directory {directory}, it already exist.")

        # Create main code file
        if not os.path.exists("main.py"):
            with open("main.py","+wt") as file:
                file.write("from frostlight_engine import *\n")
                file.write("\n")
                file.write("class Game(Engine):\n")
                file.write("    def __init__(self):\n")
                file.write("        super().__init__() # Engine options go here\n")
                file.write("\n")
                file.write("    def update(self):\n")
                file.write('        if self.game_state == "intro":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "menu":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "game":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write("    def draw(self):\n")
                file.write('        if self.game_state == "intro":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "menu":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write('        if self.game_state == "game":\n')
                file.write("            pass\n")
                file.write("\n")
                file.write("\n")
                file.write('if __name__ == "__main__":\n')
                file.write("    game = Game()\n")
                file.write("    game.run()\n")
            files_created += 1
        else:
            self.engine.logger.warning("Skipping creation of main file, already exist.")

        # Log creation process
        if files_created == 0 and directories_created == 0:
            self.engine.logger.info("No new files or directories where created.")
        else:
            self.engine.logger.info(f"Created game files structure with {files_created} files and {directories_created} directories")

    def create_exe(self,name:str="game"):

        # Import Modules
        import subprocess
        import shutil
        import sys

        # Install pyinstaller
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            import PyInstaller.__main__
        except:
            print("Pyinstaller cannot be installed!")
        else:

            # Packing game in exe
            PyInstaller.__main__.run([
                'main.py',
                '--onefile',
                '--noconsole',
                '--clean'
            ])

            # Removing build files
            if os.path.isfile("main.spec"):
                os.remove("main.spec")
            if os.path.isdir("build"):
                shutil.rmtree("build")
            if os.path.isdir("dist"):
                if os.path.isdir("export"):
                    shutil.rmtree("export")
                os.rename("dist","export")

            # Create Export DIR
            if os.path.isdir("data"):
                shutil.copytree("data",os.path.join("export","data"))
            if os.path.isdir("screenshots"):
                shutil.copytree("screenshots",os.path.join("export","screenshots"))

            # Zip Export
            if os.path.isdir("export"):
                shutil.make_archive("export","zip","export")
                shutil.rmtree("export")

    def pack_release(self):
        
        # Relevent paths 
        class_path = "./classes"
        export_file = "engine_export.py"
        main_file = "frostlight_engine.py"
        imported_modules = []

        # read class folder 
        for pathname, _, files in os.walk(class_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(pathname, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        for line in content.split("\n"):
                            if line.strip().startswith("import ") or line.strip().startswith("from "):
                                if not line.strip().startswith("from classes."):
                                    imported_modules.append(line.strip())

        imported_modules = sorted(set(imported_modules))

        # read main file
        with open(main_file, "r", encoding="utf-8") as main_handle:
            main_content = main_handle.read()

            for line in main_content.split("\n"):
                if line.strip().startswith("import ") or line.strip().startswith("from "):
                    if not line.strip().startswith("from classes."):
                        imported_modules.append(line.strip())

        imported_modules = sorted(set(imported_modules))

        # creating export file
        with open(export_file, "w", encoding="utf-8") as f:
            for importzeile in imported_modules:
                f.write(f"{importzeile}\n")
            f.write("\n") 
            for pathname, _, files in os.walk(class_path):
                for file in files:
                    if file.endswith(".py"):
                        file_path = os.path.join(pathname, file)
                        with open(file_path, "r", encoding="utf-8") as c:
                            content = c.read()
                            for importzeile in imported_modules:
                                content = content.replace(importzeile, "")
                            content = "\n".join(line for line in content.split("\n") if line.strip() and not line.strip().startswith("from classes."))
                            f.write(content.strip())
                        f.write("\n\n")

            main_content = "\n".join(line for line in main_content.split("\n") if line.strip() and not line.strip().startswith("from classes.") and not line.strip().startswith("import "))
            f.write(main_content)