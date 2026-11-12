
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
import constants
from pieces import piece, pawn, rook, knight, bishop, queen, king

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
        - occupying_piece: Piece object that occupies the square. 
                           Set to none on creation, updated when
                           a piece is given a sqaure in set_occupying_piece()

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

        # Initialize the occupying piece
        self.occupying_piece = None

        # Determine surrounding spaces
        self.__init_surrounding_spaces()

        return

    def __init_surrounding_spaces(self):
        """
        Builds a list of surrounding spaces based on name.
        
        Args:
            None

        Returns:
            None
        """
        self.surrounding_spaces = []

        for space in constants.space_names:
            space_col = space[0]
            space_row = space[1]

            # Assign to variables for readibility
            col_delta = abs(constants.board_col_labels.index(space_col) - constants.board_col_labels.index(self.square_col))
            row_delta = abs(constants.board_row_labels.index(space_row) - constants.board_row_labels.index(self.square_row))

            if space != self.name and col_delta <= 1 and row_delta <= 1:
               
                # Space is adjacent. Add it to the list
                self.surrounding_spaces.append(space)

    
    @property
    def square_col(self)->str:
        """
        Return's piece's occupied square column letter as a string.
        Args:
            None

        Returns:
            square_col: piece's occupied square column letter as a string ("A", "B", "C"...)    
        """
        return self.name[0]
    
    @property
    def square_row(self)->str:
        """
        Return's piece's occupied square row number as a str.
        Args:
            None

        Returns:
            square_row: piece's occupied square row number as a str ("1", "2", "3"...)    
        """
        return self.name[1]    

    def draw_square(self):
        """
        Draws the square at its position values

        Args:
            None

        Returns:
            None
        """
        # self.length used as both height and width args to ensure square shape
        arcade.draw_rect_filled(arcade.rect.XYWH(self.center_x, self.center_y, self.length, self.length), self.color)
        return

    def remove_occupying_piece(self):
        """
        Method to remove the space's occupying piece

        Args:
            None

        Returns:
            None       
        """
        self.occupying_piece = None

    def set_occupying_piece(self, piece_to_set:piece.Piece):
        """
        Set the space's occupying piece. The piece's sprite is also updated
        to ensure the sprite follows the piece. 
        """
        # Set occupying piece reference
        self.occupying_piece = piece_to_set

        # Update the piece sprite's position to match the square
        self.occupying_piece.sprite.center_x = self.center_x
        self.occupying_piece.sprite.center_y = self.center_y

        # Update the sprite's scale to always fit in the square
        try:
            self.occupying_piece.sprite.scale = self.length/self.occupying_piece.image_width
        except Exception:
            # Probably tried to divide by 0
            self.occupying_piece.sprite.scale = 1
