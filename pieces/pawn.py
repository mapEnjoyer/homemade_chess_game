"""
File name: pawn.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains class/logic for pawns.
"""
import constants
import arcade
from visuals import board_space

class Pawn():
    """
    Pawn class. Allows for the creation of pawn pieces, the creation of 
    their sprite objects and the ability to move around the chess board. 
    Attributes:
        - occupied_space: board space object. Used to set which square the
                          piece is on and draw the sprite on the screen. 

        - sprite: arcade sprite object. Used to draw the piece on the board.
                  Requires a valid texture path.
    """
    def __init__(self, space: board_space.Board_Space, texture_path:str):
        """
        Initializes pawn object by performing the following steps:
            - Creating sprite
            - Setting occupied square

        Args:
            space: Board_Space object the piece occupies
            texture_path: str to image file used for piece sprite.

        Returns:
            None
        """
        # Create occupied_square attribute (will be set in update_space())
        self.occupied_square = None

        # Create the pawn sprite from the texture path (TODO: error handling on path?)
        self.sprite = arcade.Sprite(texture_path)

        # Set the occupying space
        self.update_space(space)

        return
    
    def update_space(self, space: board_space.Board_Space):
        """
        Updates the space the pawn occupies

        Args:
            space: Board_Space object the piece occupies

        Returns:
            None
        """
        # Save the square the pawn occupies 
        self.occupied_square = space

        # Update the pawn sprite's position to match the square
        self.sprite.center_x = self.occupied_square.center_x
        self.sprite.center_y = self.occupied_square.center_y
        # Update the sprite's scale to always fit in the square
        try:
            self.sprite.scale = self.occupied_square.length/constants.pawn_image_width
        except:
            # Probably tried to divide by 0
            self.sprite.scale = 1

        return