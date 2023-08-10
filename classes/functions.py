import os
def create_file_structure():
    directories_created = 0
    files_created = 0
    directories_to_create = ["data","screenshots",os.path.join("data","classes"),os.path.join("data","saves"),os.path.join("data","sprites")]

    if not os.path.exists(os.path.join("data","log.txt")):
        files_created += 1

    for directory in directories_to_create:
        try:
            os.mkdir(directory)
            directories_created += 1
        except FileExistsError:
            pass
            # log(f"Skipping creation of directory {directory}, it already exist.")

    if not os.path.exists("main.py"):
        with open("main.py","+wt") as file:
            file.write("from frostlight_engine import Engine\n")
            file.write("\n")
            file.write("class Game(Engine):\n")
            file.write("    def __init__(self):\n")
            file.write("        super().__init__()\n")
            file.write("\n")
            file.write("    def update(self):\n")
            file.write("        super().update()\n")
            file.write("\n")
            file.write('        if self.game_state == "intro":\n')
            file.write("            pass\n")
            file.write("\n")
            file.write('        if self.game_state == "menu":\n')
            file.write("            pass\n")
            file.write("\n")
            file.write('        if self.game_state == "game":\n')
            file.write("            pass\n")
            file.write("\n")
            file.write('        if self.game_state == "credits":\n')
            file.write("            pass\n")
            file.write("\n")
            file.write("    def draw(self):\n")
            file.write("        super().draw()\n")
            file.write("\n")
            file.write('        if self.game_state == "intro":\n')
            file.write("            pass\n")
            file.write("\n")
            file.write('        if self.game_state == "menu":\n')
            file.write("            pass\n")
            file.write("\n")
            file.write('        if self.game_state == "game":\n')
            file.write("            pass\n")
            file.write("\n")
            file.write('        if self.game_state == "credits":\n')
            file.write("            pass\n")
            file.write("\n")
            file.write('if __name__ == "__main__":\n')
            file.write("    game = Game()\n")
            file.write("    game.run()\n")
        files_created += 1
    # else:
    #     log("Skipping creation of main file, already exist.")

    # if files_created == 0 and directories_created == 0:
    #     log("No new files and directories where created.")
    # else:
    #     log(f"Created game files structure with {files_created} files and {directories_created} directories")