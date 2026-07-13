"""
File name: board_space.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains the necessary classes, functions, methods, etc.
    maintaining an individual space on the chess board.
"""

import arcade

class Board_Space():
    """
    Board space class. Manages each space on the board, 
    and allows pieces to know where they are on the board.

    Attributes:
        - center_x: Square's center x position in the window
        - center_y: Square's center y position in the window
        - length: Length of the sqaure edge
        - color: Color of the sqaure
        - name: Name of the square on the board (A1, A2...)
    """
    
    def __init__(self, center_x: float = 0, center_y: float = 0, length: float = 0, color: arcade.color = arcade.color.WHITE, name: str = 'A1'):
        """
        Initializes space object
        
        Args:
            center_x: Center x position of the space
            center_y: Center y position of the space
            length:   Length of square
            color:    Color of the square
            name:     Name of the square based on row and column it occupies

        Returns:
            None
        """
        
        # Assign property values
        self.center_x = center_x
        self.center_y = center_y
        self.length = length
        self.color = color
        self.name = name

        return

    def draw_square(self):
        """
        Draws the square at its position values

        Args:,
            None

        Returns:
            None
        """
        # self.length used as both height and width args to ensure square shape
        arcade.draw_rect_filled(arcade.rect.XYWH(self.center_x, self.center_y, self.length, self.length), self.color)
        return
