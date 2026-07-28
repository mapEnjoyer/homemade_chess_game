"""
File name: rook.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains class/logic for rooks.
"""
import constants
from pieces import piece

class Rook(piece.Piece):
    """
    Rook class. Allows for the creation of rook pieces, the creation of 
    their sprite objects and the ability to move around the chess board. 
    Attributes:
        - occupied_space: board space object. Used to set which square the
                          piece is on and draw the sprite on the screen. 

        - sprite: arcade sprite object. Used to draw the piece on the board.
                  Requires a valid texture path.

        - image_width: Width in pixels of the image used in the sprite.
    """
    def __init__(self, space: piece.Board_Space, texture_path:str, image_width:int):
        """
        Initializes rook object by performing the following steps:
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

    def is_move_valid(self, space:str):
        """
        Method to determine if the rook object can "theoretically" move to the indicated square.
        Valid rook moves include:
            - going diagonal in any direction

        Args:
            space: Destination space string name for the rook to move to ('A1', 'A2'...)

        Returns:
            move_is_valid: True if the move is "theoretically" possible (not including pieces blocking the way/captures not being present)
        """
        cur_col_idx = constants.board_col_labels.index(self.occupied_square.square_col)
        cur_row_idx = constants.board_row_labels.index(self.occupied_square.square_row)
        nxt_col_idx = constants.board_col_labels.index(space[0])
        nxt_row_idx = constants.board_row_labels.index(space[1])

        # Rook moves are valid if the piece is moving 
        # along the same row or column it is starting in.
        return (cur_col_idx == nxt_col_idx and cur_row_idx != nxt_row_idx) or \
               (cur_col_idx != nxt_col_idx and cur_row_idx == nxt_row_idx)