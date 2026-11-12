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

class Piece(ABC):
    """
    Piece class. This class is intended to be used as the parent for the other
    pieces, not to be used on it's on.
    Attributes:
        - sprite: arcade sprite object. Used to draw the piece on the board.
                  Requires a valid texture path.

        - has_moved: Boolean indicator indicating if piece has moved before.
        - color: Color of piece. Can either be black or white
    """
    def __init__(self, texture_path:str, image_width:int, color:constants.PlayerColor):
        """
        Initializes piece object by performing the following steps:
            - Creating sprite
            - setting color

        Args:
            color: Color of piece. Can either be black or white
        Returns:
            None
        """

        # Create the piece sprite from the texture path (TODO: error handling on path?)
        self.sprite = arcade.Sprite(texture_path)

        # Save the image width
        self.image_width = image_width

        # Set has moved indicator to false
        self.has_moved = False

        # Set piece color
        self.color = color

        return
    
    @abstractmethod
    def is_move_valid(space:str):
        pass
