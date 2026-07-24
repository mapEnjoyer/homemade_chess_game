"""
File name: pawn.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains class/logic for pawns.
"""
import constants
from pieces import piece

class Pawn(piece.Piece):
    """
    Pawn class. Allows for the creation of pawn pieces, the creation of 
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
        Initializes pawn object by performing the following steps:
            - Creating sprite
            - Setting occupied square

        Args:
            space: Board_Space object the piece occupies
            texture_path: str to image file used for piece sprite.

        Returns:
            None
        """
        self.color = None

        # Run parent class init
        super().__init__(space, texture_path, image_width)

        return

    def is_move_valid(self, space:str):
        """
        Method to determine if the pawn object can "theoretically" move to the indicated square.
        Valid pawn moves include:
            - Going 1 square "forward" (depends on color of pawn) in the same column
            - Going 1 square "forward" diagonally if capturing (requires the board to determine that).
            - Going 2 squares "forward" if the pawn has not moved yet.

        Because pawns can only move in one direction, we need to take special consideration on what
        constitues as "forward" for a pawn. For white pawns, "forward" means incrementing row numbers.
        For black pawns the opposite is true. 

        Args:
            space: Destination space string name for the pawn to move to ('A1', 'A2'...)

        Returns:
            move_is_valid: True if the move is "theoretically" possible (not including pieces blocking the way/captures not being present)
        """
        valid_spaces = []

        # Intitialize variables for readability
        cur_col = constants.board_col_labels.index(self.occupied_square.square_col)
        cur_row = constants.board_row_labels.index(self.occupied_square.square_row)
        max_col = len(constants.board_col_labels) - 1

        # Determine direction value based on color
        if self.color == constants.PlayerColor.WHITE:
            direction = 1 # positive means "forward" is incrementing row count
        else:
            direction = -1 # negative means "forward" is decrementing row count

        # It is mandatory for a pawn to promote once it reaches either edge of the board.
        # This code assumes no pawn would exist on the first or last row since it would promote. 
        # Pawn can always move 1 space ahead or diagonally if they are capturing.
        
        # Add space immediately ahead
        valid_spaces.append(constants.board_col_labels[cur_col] + constants.board_row_labels[cur_row + direction])

        if cur_col > 0:
            # Add space diagonally towards A
            valid_spaces.append(constants.board_col_labels[cur_col - 1] + constants.board_row_labels[cur_row + direction])

        if cur_col < max_col:
            # Add space diagonally towards H
            valid_spaces.append(constants.board_col_labels[cur_col + 1] + constants.board_row_labels[cur_row + direction])

        # Pawn can move 2 spaces if it hasn't moved yet
        if self.has_moved == False:
            valid_spaces.append(constants.board_col_labels[cur_col] + constants.board_row_labels[cur_row+2*direction])

        return space in valid_spaces
