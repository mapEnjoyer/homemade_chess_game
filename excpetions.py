"""
File name: exceptions.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 07/12/26

@brief: 
    This file contains shared customs excpetions used throughout the project.
"""
class InvalidPieceTypeError(Exception):
    """
    Custom exception handler for when user tries to move piece of a type that doesn't exist
    """
    
    def __init__(self):

        """
        Notifies the player that the move they have entered references a piece type
        that does not exist.

        Args:
            None

        Returns:
            None
        """
        super().__init__()

class InvalidSpaceError(Exception):
    """
    Custom exception handler for when user tries to move piece to a square that doesn't exist
    """
    
    def __init__(self):

        """
        Notifies the player that the move they have entered references a piece type
        that does not exist.

        Args:
            None
            
        Returns:
            None
        """
        super().__init__()