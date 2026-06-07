"""
File name: board.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains the necessary classes, functions, methods, etc.
    maintaining the checkerboard pattern of the chess game.
"""

import arcade

# List of all board spaces as strings
space_names =  ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
                "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8",
                "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
                "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8",
                "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8",
                "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8",
                "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8",]

class board():
    """
    Board class. Used to access all spaces on the board.
    Args:
        None

    Returns:
        None    
    """

    def __init__(self):

        # Dictonary containing all board spaces. Initialized in board_init
        # {"A1" : board_space A1; "A2": board_space A2; ...}
        self.board_spaces = {}

        # A1 is black on chess board
        space_color = arcade.color.BLACK
        row_count = 0

        for name in space_names:
            
            # Update row_count 
            row_count = int(name[1])

            # Create a space class for each space
            self.board_spaces[name] = board_space(color = space_color)

            if row_count != 8:
                if space_color == arcade.color.BLACK:
                    # Swap color to tan
                    space_color = arcade.color.TAN

                else:
                    # Swap color back to black
                    space_color = arcade.color.BLACK       
        
class board_space():
    """
    Board space class. Manages each space on the board, 
    and allows pieces to know where they are on the board.

    Args:
        center_x: Center x position of the space
        center_y: Center y position of the space
        length:   Length of square
        color:    Color of the square

    Returns:
        None

    """
    
    def __init__(self, center_x: float = 0, center_y: float = 0, length: float = 0, color: arcade.color = arcade.color.WHITE):
        """
            Initializes space object
        """
        
        # Assign property values
        self.center_x = center_x
        self.center_y = center_y
        self.length = length
        self.color = color

        return

    def draw_square(self):
        """
        Draws the square at its position values

        Args:,
            None

        Returns:
            None
        """
        arcade.draw_rect_filled(arcade.rect.XYWH(self.center_x, self.center_y, self.length, self.length), self.color)
        return
