"""
File name: knight.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains class/logic for knights.
"""
import constants
from pieces import piece

class Knight(piece.Piece):
    """
    Knight class. Allows for the creation of knight pieces, the creation of 
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
        Initializes knight object by performing the following steps:
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
        Method to determine if the knight object can "theoretically" move to the indicated square.
        Valid knight moves include:
            - going vertical 2 spaces then horizontal 1
            - going horizontal 2 spaces then vertical 1

        Args:
            space:  Destination space string name for the knight to move to ('A1', 'A2'...)

        Returns:
            move_is_valid: True if the move is "theoretically" possible (not including pieces blocking the way/captures not being present)
        """
        valid_spaces = []

        # Note that rows and columns are indexed between 0-7
        col_idx = constants.board_col_labels.index(self.occupied_square.square_col)
        row_num = constants.board_row_labels.index(self.occupied_square.square_row)
        min_col = 0
        max_col = len(constants.board_col_labels) - 1
        min_row = 0
        max_row = len(constants.board_row_labels) - 1        
        
        # Check 2 rows towards row 8 and 1 towards A
        if row_num < max_row - 1 and col_idx > min_col:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-1] + constants.board_row_labels[row_num+2])

        # Check 2 rows towards row 8 and 1 towards H
        if row_num < max_row - 1 and col_idx < max_col:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+1] + constants.board_row_labels[row_num+2])           

        # Check 2 rows towards row 1 and 1 towards A
        if row_num > min_row + 1 and col_idx > min_col:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-1] + constants.board_row_labels[row_num-2])
    
        # Check 2 rows towards row 1 and 1 towards H
        if row_num > min_row + 1 and col_idx < max_col:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+1] + constants.board_row_labels[row_num-2])

        # Check 2 columns towards A and 1 towards row 8 
        if col_idx > min_col + 1 and row_num < max_row:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-2] + constants.board_row_labels[row_num+1])

        # Check 2 columns towards A and 1 towards row 1
        if col_idx > min_col + 1 and row_num > min_row:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-2] + constants.board_row_labels[row_num-1])

        # Check 2 columns towards H and 1 towards row 8
        if col_idx < max_col - 1 and row_num < max_row:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+2] + constants.board_row_labels[row_num+1])

        # Check 2 columns towards H and 1 towards row 1
        if col_idx < max_col - 1 and row_num > min_row:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+2] + constants.board_row_labels[row_num-1])

        return space in valid_spaces
