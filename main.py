"""
File name: main.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file is the top level execution of my homemade chess application.
"""

import arcade
from visuals import window

"""
Function Name: main

    Main function call for the chess application

    Args:
        None

    Returns:
        None
"""
if __name__ == "__main__":
    # Initialize the application window
    window.window_init()

    arcade.run()
    