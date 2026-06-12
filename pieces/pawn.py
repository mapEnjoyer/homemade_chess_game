"""
File name: pawn.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains class/logic for pawns.
"""
import arcade
from visuals import board

class Pawn():
    """
    Pawn class. TODO: Update description
    Attributes:
        - TODO:
    """
    def __init__(self, space: board._Board_Space, texture_path:str):
        """
        Initializes pawn object by performing the following steps:
            
        """
        # Create the pawn sprite from the texture path (TODO: error handling on path?)
        self.sprite = arcade.Sprite(texture_path)

        # Set the occupying space
        self.update_space(space)

        return
    
    def update_space(self, space: board._Board_Space):
        """
        Updates the space the pawn occupies
        """
        # Save the square the pawn occupies 
        self.occupied_square = space

        # Update the pawn sprite's position to match the square
        self.sprite.center_x = self.occupied_square.center_x
        self.sprite.center_y = self.occupied_square.center_y
        self.sprite.scale = 0.04
        # # Update the sprite's scale to always fit in the square
        # try:
        #     self.sprite.scale = max(self.sprite.height, self.sprite.width)/self.occupied_square.length
        # except:
        #     # Probably tried to divide by 0
        #     self.sprite.scale = 1