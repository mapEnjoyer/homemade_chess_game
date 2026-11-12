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
from pathlib import Path

class Knight(piece.Piece):
    """
    Knight class. Allows for the creation of knight pieces, the creation of 
    their sprite objects and the ability to move around the chess board. 
    Attributes:
        - sprite: arcade sprite object. Used to draw the piece on the board.
                  Requires a valid texture path.

        - color: Color of piece. Can either be black or white
    """
    def __init__(self, color:constants.PlayerColor):
        """
        Initializes knight object by performing the following steps:
            - Creating sprite
            - setting color

        Args:
            color: Color of piece. Can either be black or white

        Returns:
            None
        """
        # Determine texture path from piece color
        if color == constants.PlayerColor.WHITE:
            texture_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.white_knight_image_name)
        else:
            texture_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.black_knight_image_name)

        # Run parent class init
        super().__init__(texture_path=texture_path, image_width=constants.knight_image_width, color=color)

        return
    
    def is_move_valid(self, curr_space:str, next_space:str):
        """
        Method to determine if the knight object can "theoretically" move to the indicated square.
        Valid knight moves include:
            - going vertical 2 spaces then horizontal 1
            - going horizontal 2 spaces then vertical 1

        Args:
            curr_space:  Starting space string name for the knight to move from ('A1', 'A2'...)
            next_space:  Destination space string name for the knight to move to ('A1', 'A2'...)

        Returns:
            move_is_valid: True if the move is "theoretically" possible (not including pieces blocking the way/captures not being present)
        """
        valid_spaces = []

        # Note that rows and columns are indexed between 0-7
        col_idx = constants.board_col_labels.index(curr_space[0])
        row_idx = constants.board_row_labels.index(curr_space[1])
        min_col = 0
        max_col = len(constants.board_col_labels) - 1
        min_row = 0
        max_row = len(constants.board_row_labels) - 1        
        
        # Check 2 rows towards row 8 and 1 towards A
        if row_idx < max_row - 1 and col_idx > min_col:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-1] + constants.board_row_labels[row_idx+2])

        # Check 2 rows towards row 8 and 1 towards H
        if row_idx < max_row - 1 and col_idx < max_col:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+1] + constants.board_row_labels[row_idx+2])           

        # Check 2 rows towards row 1 and 1 towards A
        if row_idx > min_row + 1 and col_idx > min_col:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-1] + constants.board_row_labels[row_idx-2])
    
        # Check 2 rows towards row 1 and 1 towards H
        if row_idx > min_row + 1 and col_idx < max_col:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+1] + constants.board_row_labels[row_idx-2])

        # Check 2 columns towards A and 1 towards row 8 
        if col_idx > min_col + 1 and row_idx < max_row:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-2] + constants.board_row_labels[row_idx+1])

        # Check 2 columns towards A and 1 towards row 1
        if col_idx > min_col + 1 and row_idx > min_row:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx-2] + constants.board_row_labels[row_idx-1])

        # Check 2 columns towards H and 1 towards row 8
        if col_idx < max_col - 1 and row_idx < max_row:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+2] + constants.board_row_labels[row_idx+1])

        # Check 2 columns towards H and 1 towards row 1
        if col_idx < max_col - 1 and row_idx > min_row:
            # Space is valid, add it to the list
            valid_spaces.append(constants.board_col_labels[col_idx+2] + constants.board_row_labels[row_idx-1])

        return next_space in valid_spaces
