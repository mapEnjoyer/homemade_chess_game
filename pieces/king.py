"""
File name: king.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains class/logic for kings.
"""
import constants
from pieces import piece
from pathlib import Path

class King(piece.Piece):
    """
    King class. Allows for the creation of king pieces, the creation of 
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
        Initializes king object by performing the following steps:
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
            texture_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.white_king_image_name)
        else:
            texture_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.black_king_image_name)

        # Run parent class init
        super().__init__(space=space, texture_path=texture_path, image_width=constants.king_image_width, color=color)

        return

    def is_move_valid(self, curr_space:str, next_space:str):
        """
        Method to determine if the king object can "theoretically" move to the indicated square.
        Valid king moves include:
            - going one space diagonally in any direction
            - going one space vertically or horizontally in any direction
            - castleing to either side of the board if the king has not moved yet 
              (also requires rook to have not moved, but that has to be handled at the board level)

        Args:
            curr_space: Starting space string name for the king to move from ('A1', 'A2'...)
            next_space: Destination space string name for the king to move to ('A1', 'A2'...)

        Returns:
            move_is_valid: True if the move is "theoretically" possible (not including pieces blocking the way/captures not being present)
        """
        cur_col_idx = constants.board_col_labels.index(curr_space[0])
        cur_row_idx = constants.board_row_labels.index(curr_space[1])
        nxt_col_idx = constants.board_col_labels.index(next_space[0])
        nxt_row_idx = constants.board_row_labels.index(next_space[1])

        move_is_valid = False

        # King moves are valid if they are either vertical, horizontal or diagonal one space
        move_is_valid |= abs(cur_col_idx - nxt_col_idx) <= 1 and abs(cur_row_idx - nxt_row_idx) <= 1

        # Check if the king is attemption to castle
        move_is_valid |= self.is_castleing(curr_space, next_space)

        return move_is_valid

    def is_castleing(self, curr_space:str, next_space:str):
        """
        Method to determine if the given move is a castleing move.

        Args:
            curr_space: Starting space string name for the king to move from ('A1', 'A2'...)
            next_space: Destination space string name for the king to move to ('A1', 'A2'...)

        Returns:
            is_castleing: True if the move is castleing     
        """
        is_castleing = False

        # Casteling requires king to attempt to move to C/G column from starting square as its first move
        is_castleing |= self.color == constants.PlayerColor.WHITE and (next_space == 'C1' or next_space == 'G1') and curr_space == 'E1'
        is_castleing |= self.color == constants.PlayerColor.BLACK and (next_space == 'C8' or next_space == 'G8') and curr_space == 'E8'

        return is_castleing
      