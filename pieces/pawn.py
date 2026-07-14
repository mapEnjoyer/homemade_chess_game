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

    def is_move_valid(self, space):
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
            space: Destination space for the pawn to move to

        Returns:
            move_is_valid: True if the move is "theoretically" possible (not including pieces blocking the way/captures not being present)
        """

        # Intitialize variables for readability
        new_col = constants.board_col_labels.index(space[0])
        new_row = constants.board_row_labels.index(space[1])
        cur_col = constants.board_col_labels.index(self.occupied_square.square_col)
        cur_row = constants.board_row_labels.index(self.occupied_square.square_row)
        move_is_valid = False
        adj_col = []
        
        # Determine direction value based on color
        if self.color == constants.PlayerColor.WHITE:
            direction = 1 # positive means "forward" is incrementing row count
        else:
            direction = -1 # negative means "forward" is decrementing row count
 
        if new_col == cur_col:
            # pawn can move "forward" 1 row always or 2 rows if it hasn't moved yet
            if new_row == cur_row+direction or new_row == cur_row+2*direction and self.has_moved == False:
                # Move is technically legal
                move_is_valid = True

        else:
            if cur_col-1 >= 0:
                # There is a valid column to the left
                adj_col.append(cur_col-1)

            if cur_col+1 <= len(constants.board_col_labels):
                # There is a valid column to the right
                adj_col.append(cur_col+1)

            for col in adj_col:
                # Is the move targeting one square "forward" on the adjacent column?
                if new_col == col and new_row == cur_row+direction:
                    # Move is technically legal assuming there is a capture
                    move_is_valid = True
                    break

        return move_is_valid
