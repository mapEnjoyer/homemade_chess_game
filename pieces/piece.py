"""
File name: piece.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 07/10/26

@brief: 
    This file contains the parent class that all other pieces are created from.
"""
import constants
import arcade
from visuals import board_space

class Piece():
    """
    Piece class. This class is intended to be used as the parent for the other
    pieces, not to be used on it's on.
    Attributes:
        - occupied_space: board space object. Used to set which square the
                          piece is on and draw the sprite on the screen. 

        - sprite: arcade sprite object. Used to draw the piece on the board.
                  Requires a valid texture path.

        - image_width: Width in pixels of the image used in the sprite.
    """
    def __init__(self, space: board_space.Board_Space, texture_path:str, image_width:int):
        """
        Initializes piece object by performing the following steps:
            - Creating sprite
            - Setting occupied square

        Args:
            space: Board_Space object the piece occupies
            texture_path: str to image file used for piece sprite.
            image_width: integer width of the image used for the sprite in pixels.

        Returns:
            None
        """
        # Create occupied_square attribute (will be set in update_space())
        self.occupied_square = None

        # Create the piece sprite from the texture path (TODO: error handling on path?)
        self.sprite = arcade.Sprite(texture_path)

        # Save the image width
        self.image_width = image_width

        # Set the occupying space
        self.update_space(space)

        return
    
    def update_space(self, space: board_space.Board_Space):
        """
        Updates the space the piece occupies

        Args:
            space: Board_Space object the piece occupies

        Returns:
            None
        """
        # Save the square the piece occupies 
        self.occupied_square = space

        # Update the piece sprite's position to match the square
        self.sprite.center_x = self.occupied_square.center_x
        self.sprite.center_y = self.occupied_square.center_y
        # Update the sprite's scale to always fit in the square
        try:
            self.sprite.scale = self.occupied_square.length/self.image_width
        except:
            # Probably tried to divide by 0
            self.sprite.scale = 1

        return