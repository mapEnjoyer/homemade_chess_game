"""
File name: knight.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains class/logic for knights.
"""
import constants
import arcade
from visuals import board_space

class Knight():
    """
    Knight class. TODO: Update description
    Attributes:
        - TODO:
    """
    def __init__(self, space: board_space.Board_Space, texture_path:str):
        """
        Initializes knight object by performing the following steps:
            
        """
        # Create the knight sprite from the texture path (TODO: error handling on path?)
        self.sprite = arcade.Sprite(texture_path)

        # Set the occupying space
        self.update_space(space)

        return
    
    def update_space(self, space: board_space.Board_Space):
        """
        Updates the space the knight occupies
        """
        # Save the square the knight occupies 
        self.occupied_square = space

        # Update the knight sprite's position to match the square
        self.sprite.center_x = self.occupied_square.center_x
        self.sprite.center_y = self.occupied_square.center_y
        # Update the sprite's scale to always fit in the square
        try:
            self.sprite.scale = self.occupied_square.length/constants.knight_image_width
        except:
            # Probably tried to divide by 0
            self.sprite.scale = 1

        return