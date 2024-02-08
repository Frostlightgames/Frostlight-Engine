# Frostlight-Engine

![python](https://img.shields.io/badge/python-blue) ![pygame](https://img.shields.io/badge/pygame-green) ![frostlightgames](https://img.shields.io/badge/frostlightgames-blue)

Frostlight-Engine is an easy to use game framework for python that is based on pygame. We plan on making an entire game engine some day.

## **Overview**

- [Frostlight-Engine](#frostlight-engine)
  - [**Overview**](#overview)
  - [**Getting Started**](#getting-started)
  - [**Dependencies**](#dependencies)
  - [**Making a game**](#making-a-game)
  - [**Example**](#example)

## **Getting Started**

1.  Install Python 3.9 or newer. \<https://www.python.org/downloads/\>
2.  Install pygame/pygame-ce 2.x \<https://pypi.org/project/pygame/\>
3.  Download the newest Frostlight-Engine version \<https://github.com/Frostlightgames/Frostlight-Engine\>

```
pip install pygame | pip install pygame-ce
```

## **Dependencies**

- python 3.9 or newer
- pygame 2.0 or newer
- cryptography

## **Making a game**

Frostlight-Engine is a single-file framework, that helps you create games very fast and efficient. The game logic will be written in python. You can use any text editor you want. Frostlight-Engine provides some tool like window or input management to simplify the game making process.

1.  Create an empty directory and paste the `frostlight_engine.py` file in it
2.  Run `frostlight_engine.py` in your terminal, it will setup your project structure

```
python frostlight_engine.py
```

In the `main.py` file you will write your main game logic. Your `Game` class will inherit from the `frostlight_engine.py` file to have all the framework functionality. To make your first little demo copy the example code into the `main.py` file.

## **Example**

```python
from frostlight_engine import *

class Game(Engine):
    def __init__(self):
        super().__init__(window_size=[800,800])

        # Create player sprite
        self.player_sprite = pygame.Surface((100,100))
        self.player_sprite.fill((10,126,221))

        # Loading player pos from save file
        self.player_pos = pygame.Vector2(self.save_manager.load("pos",[350,350]))

        # Switching game state
        self.game_state = "game"

    def update(self):
        if self.game_state == "game":

            # Renaming window
            self.window.set_name(f"FPS: {self.window.get_fps()}")

            # Calculating player x velocity
            x_vel = self.input.get("right")-self.input.get("left")
            self.player_pos.x += x_vel*200*self.delta_time

            # Calculating player y velocity
            y_vel = self.input.get("down")-self.input.get("up")
            self.player_pos.y += y_vel*200*self.delta_time

            # Writing player position to save file
            self.save_manager.save("pos",[self.player_pos[0],self.player_pos[1]])

    def draw(self):
        if self.game_state == "game":

            # Draw background and player
            self.window.fill([3,13,36])
            self.window.render(self.player_sprite,self.player_pos)

if __name__ == "__main__":
    game = Game()
    game.run()
```

Now you can run your game by typing the following in your terminal:

```
python main.py
```

If you now want to share your game with friends, that don't have python installed, you can just pack your game into an executable by running:

```
python frostlight_engine.py -b | python frostlight_engine.py --build
```

Your game will be compressed into a zip archive called `export.zip` that you can now send to a friend.

### **Features**

- Window management
- Input management
  - Keyboard
  - Mouse
  - Controller
    - XBox 360
    - Playstation 4
    - Playstation 5
    - Nintendo Switch Pro Controller
    - Nintendo Switch Joy Cons
- Logging
- Save managing
- Error catching and handling
- EXE converting
- Automatic project setup

### **Project Structure**

```
📁game_name                 # your created root directory.
    📁data                  # store important game data
        📁classes           # to store your game classes like player and monsters
        📁saves             # to store progress saves and input configurations
            📁backup        # to store your backed up save files
        📁sprites           # to store your game sprites or fonts
    📁logs                  # to collect your game and engine logs
    📁screenshots           # to collect your game screenshots

    📃frostlight_engine.py  # single frostlight-engine file
    📃main.py               # your main game logic
```
