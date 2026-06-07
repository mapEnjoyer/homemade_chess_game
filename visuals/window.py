"""
File name: main.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains the necessary classes, functions, methods, etc.for
    creating and maintaining the window settings for the chess game.  
"""
import arcade
from pathlib import Path

# Window Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 1040
WINDOW_TITLE = "EAKs Chess Game"

class GameView(arcade.Window):
    """
    Main application class. Handles visuals for the game
    """

    def __init__(self):

        # Call the parent class to set up the window
        # TODO: Probably want to save these settings in a user_config.json 
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)

        # Set window settings
        self.background_color = arcade.csscolor.DARK_OLIVE_GREEN # Background color

        # Set path to visuals
        visuals_path = Path.cwd()._str + '/visuals'

        # TODO: Load textures and sprites

        return

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here

        # TODO: Draw the chess board

        return


"""
Function Name: window_init

    Initializes the window containing game visuals

@param  None
@return None
"""
def window_init():
    # Create a instance of the GameView class
    window = GameView()
    window.setup()

    return
