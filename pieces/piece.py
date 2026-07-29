"""
File name: piece.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 07/10/26

@brief: 
    This file contains the parent class that all other pieces are created from.
"""
import constants
import arcade
from abc import ABC, abstractmethod

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
        - occupying_piece: Piece object that occupies the square. 
                           Set to none on creation, updated when
                           a piece is given a sqaure in update_space()

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

        return
    
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

        Args:,
            None

        Returns:
            None
        """
        # self.length used as both height and width args to ensure square shape
        arcade.draw_rect_filled(arcade.rect.XYWH(self.center_x, self.center_y, self.length, self.length), self.color)
        return

class Piece(ABC):
    """
    Piece class. This class is intended to be used as the parent for the other
    pieces, not to be used on it's on.
    Attributes:
        - occupied_space: board space object. Used to set which square the
                          piece is on and draw the sprite on the screen. 

        - sprite: arcade sprite object. Used to draw the piece on the board.
                  Requires a valid texture path.

        - image_width: Width in pixels of the image used in the sprite.

        - has_moved: Boolean indicator indicating if piece has moved before.
        - color: Color of piece. Can either be black or white depending on which row the piece is created on
    """
    def __init__(self, space: Board_Space, texture_path:str, image_width:int):
        """
        Initializes piece object by performing the following steps:
            - Creating sprite
            - Setting occupied square

        Args:
            space: Board_Space object the piece occupies
            texture_path: str to image file used for piece sprite.
            image_width: integer width of the image used for the sprite in pixels.

        Returns:
            None
        """
        # Create occupied_square attribute (will be set in update_space())
        self.occupied_square = None

        # Create the piece sprite from the texture path (TODO: error handling on path?)
        self.sprite = arcade.Sprite(texture_path)

        # Save the image width
        self.image_width = image_width

        # Set has moved indicator to false
        self.has_moved = False

        # Set the occupying space
        self.update_space(space)

        # Use row the piece was created on (<=2 = white, >=7 = black) to determine color
        if int(self.occupied_square.name[1]) <= 2:
            self.color = constants.PlayerColor.WHITE
        elif int(self.occupied_square.name[1]) >= 7:
            self.color = constants.PlayerColor.BLACK

        return    
    
    def update_space(self, space: Board_Space):
        """
        Updates the space the piece occupies

        Args:
            space: Board_Space object the piece occupies

        Returns:
            None
        """
        # Need this if statement since occupied_square is None until first square is assigned
        if isinstance(self.occupied_square, Board_Space):
            # Clear the occupying_piece attribute of the space the piece is leaving
            self.occupied_square.occupying_piece = None

        # Save the square the piece occupies 
        self.occupied_square = space

        # Update the occupying_piece attribute of the space now that a new piece is on the square
        self.occupied_square.occupying_piece = self

        # Update the piece sprite's position to match the square
        self.sprite.center_x = self.occupied_square.center_x
        self.sprite.center_y = self.occupied_square.center_y
        # Update the sprite's scale to always fit in the square
        try:
            self.sprite.scale = self.occupied_square.length/self.image_width
        except:
            # Probably tried to divide by 0
            self.sprite.scale = 1

        return
    
    @abstractmethod
    def is_move_valid(space:str):
        pass
