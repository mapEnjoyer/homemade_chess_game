"""
File name: queen.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains class/logic for queens.
"""
from pieces import piece
from visuals import board_space

class Queen(piece.Piece):
    """
    Queen class. Allows for the creation of queen pieces, the creation of 
    their sprite objects and the ability to move around the chess board. 
    Attributes:
        - occupied_space: board space object. Used to set which square the
                          piece is on and draw the sprite on the screen. 

        - sprite: arcade sprite object. Used to draw the piece on the board.
                  Requires a valid texture path.

        - image_width: Width in pixels of the image used in the sprite.
    """
    def __init__(self, space: board_space.Board_Space, texture_path:str, image_width:int):
        """
        Initializes queen object by performing the following steps:
            - Creating sprite
            - Setting occupied square

        Args:
            space: Board_Space object the piece occupies
            texture_path: str to image file used for piece sprite.
            image_width: integer width of the image used for the sprite in pixels.

        Returns:
            None
        """
        # Run parent class init
        super().__init__(space, texture_path, image_width)

        return