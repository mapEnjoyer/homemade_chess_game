"""
File name: queen.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains class/logic for queens.
"""
import constants
from pieces import piece
from pathlib import Path

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
        - color: Color of piece. Can either be black or white
    """
    def __init__(self, space: piece.Board_Space, color:constants.PlayerColor):
        """
        Initializes queen object by performing the following steps:
            - Creating sprite
            - Setting occupied square

        Args:
            space: Board_Space object the piece occupies
            color: Color of piece. Can either be black or white

        Returns:
            None
        """
        # Determine texture path from piece color
        if color == constants.PlayerColor.WHITE:
            texture_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.white_queen_image_name)
        else:
            texture_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.black_queen_image_name)

        # Run parent class init
        super().__init__(space=space, texture_path=texture_path, image_width=constants.queen_image_width, color=color)

        return

    def is_move_valid(self, space:str):
        """
        Method to determine if the queen object can "theoretically" move to the indicated square.
        Valid queen moves include:
            - going diagonal in any direction
            - going vertical or horizontal in any direction

        Args:
            space: Destination space string name for the queen to move to ('A1', 'A2'...)

        Returns:
            move_is_valid: True if the move is "theoretically" possible (not including pieces blocking the way/captures not being present)
        """
        cur_col_idx = constants.board_col_labels.index(self.occupied_square.square_col)
        cur_row_idx = constants.board_row_labels.index(self.occupied_square.square_row)
        nxt_col_idx = constants.board_col_labels.index(space[0])
        nxt_row_idx = constants.board_row_labels.index(space[1])

        move_is_valid = False

        # Queen moves are valid if they are either vertical, horizontal or diagonal
        move_is_valid |= abs(cur_col_idx - nxt_col_idx) == abs(cur_row_idx - nxt_row_idx) # Diagonal check
        move_is_valid |= cur_col_idx == nxt_col_idx and cur_row_idx != nxt_row_idx # Vertical check
        move_is_valid |= cur_col_idx != nxt_col_idx and cur_row_idx == nxt_row_idx # Horizontal check

        return move_is_valid