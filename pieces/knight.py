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

        Returns:
            None
        """
        # Run parent class init
        super().__init__(space, texture_path, image_width)

        return
    
    def is_move_valid(self, space):
        """
        Method to determine if the knight object can "theoretically" move to the indicated square.
        Valid knight moves include:
            - going vertical 2 spaces then horizontal 1
            - going horizontal 2 spaces then vertical 1

        Args:
            space: Destination space for the knight to move to

        Returns:
            move_is_valid: True if the move is "theoretically" possible (not including pieces blocking the way/captures not being present)
        """
        valid_spaces = []
        move_is_valid = False

        # Note that columns are indexed between 0-7 but row numbers are 1-8
        col_idx = constants.board_col_labels.index(self.occupied_square.square_col)
        row_num = self.occupied_square.square_row
        
        # Check 2 rows up and 1 left (white perspective)
        if row_num < 7 and col_idx > 0:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-1] + str(row_num+2))

        # Check 2 rows up and 1 right (white perspective)
        if row_num < 7 and col_idx < 8:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+1] + str(row_num+2))            

        # Check 2 rows down and 1 left (white perspective)
        if row_num > 2 and col_idx > 0:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-1] + str(row_num-2))
    
        # Check 2 rows down and 1 right (white perspective)
        if row_num > 2 and col_idx < 8:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+1] + str(row_num-2))

        # Check 2 columns left and 1 up (white perspective)
        if col_idx > 1 and row_num < 8:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-2] + str(row_num+1))

        # Check 2 columns left and 1 down (white perspective)
        if col_idx > 1 and row_num > 1:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-2] + str(row_num-1))

        # Check 2 columns right and 1 up (white perspective)
        if col_idx < 7 and row_num < 8:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+2] + str(row_num+1))

        # Check 2 columns right and 1 down (white perspective)
        if col_idx < 7 and row_num > 1:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+2] + str(row_num-1))

        move_is_valid = space in valid_spaces
        return move_is_valid