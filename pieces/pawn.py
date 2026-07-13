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
        - color: Because pawns are the only piece that can move 1 direction, they need
                 to know what color they are for move validity checks.
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

        # Use row the pawn was created on (2 = white, 7 = black) to determine color
        if int(self.occupied_square.name[1]) == 2:
            self.color = "white"
        elif int(self.occupied_square.name[1]) == 7:
            self.color = "black"

        return

    def is_move_valid(self, space):
        """
        Method to determine if the pawn object can "theoretically" move to the indicated square.
        Valid pawn moves include:
            - Going 1 square "forward" (depends on color of pawn) in the same column
            - Going 1 square "forward" diagonally if capturing (requires the board to determine that).
            - Going 2 squares "forward" if the pawn has not moved yet. 

        Args:
            space: Destination space for the pawn to move to

        Returns:
            move_is_valid: True if the move is "theoretically" possible (not including pieces blocking the way/captures not being present)
        """

        # Intitialize variables for readability
        new_col = space[0]
        new_row = int(space[1])
        cur_col = self.occupied_square.name[0]
        cur_row = int(self.occupied_square.name[1])
        move_is_valid = False
        adj_col = []
        
        # Determine direction value based on color
        if self.color == 'white':
            direction = 1 # positive means "forward" is incrementing row count
        else:
            direction = -1 # negative means "forward" is decrementing row count
 
        if new_col == cur_col:
            # pawn can move "forward" 1 row always or 2 rows if it hasn't moved yet
            if new_row == ((cur_row+1)*direction) or (new_row == ((cur_row+2)*direction) and self.has_moved == False):
                # Move is technically legal
                move_is_valid = True

        else:
            # Pawn could be moving on the diagonal, determine which columns are adjacent
            col_idx = constants.board_col_labels.index(cur_col)

            if col_idx-1 >= 0:
                # There is a valid column to the left
                adj_col.append(constants.board_col_labels[col_idx-1])

            if col_idx+1 <= len(constants.board_col_labels):
                # There is a valid column to the right
                adj_col.append(constants.board_col_labels[col_idx+1])

            for col in adj_col:
                # Is the move targeting one square "forward" on the adjacent column?
                if new_col == col and new_row == ((cur_row+1)*direction):
                    # Move is technically legal assuming there is a capture
                    move_is_valid = True
                    break

        return move_is_valid
