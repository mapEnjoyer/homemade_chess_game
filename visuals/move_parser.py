"""
File name: move_parser.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 07/03/26

@brief: 
    This file contains the necessary classes, functions, methods, etc.
    for handling user text input (and eventually mouse inputs) for moving
    pieces around the chess board.
"""

import pyglet
import arcade

class MoveParser():
    """
    Move parser class. Used to handle text input (and eventually mouse inputs)
    for players to move pieces around the chess board.

    Attributes:
        TBD
    """

    def __init__(self, window:arcade.Window):
        """
        Initializes the move parser by performing the following steps:
            TBD

        Args:
            window: arcade window object the text entry is apart of. This is to 
                    ensure text box reacts to inputs in the window it occupies.

        Returns:
            None
        """
    
        # Text entry window
        # The only way I could find to get the text box widget
        # to appear on screen was to make it apart of a "batch" 
        # and call the batch.draw() method on each frame.
        self.text_batch = pyglet.graphics.Batch()

        # x, y and width does not matter as the window will have 
        # to reassign these settings based on the size of the window.
        self.text_entry = pyglet.gui.TextEntry(text="Test", 
                                               x=0, 
                                               y=0, 
                                               width=300, 
                                               batch=self.text_batch, 
                                               color=arcade.csscolor.BLACK, 
                                               text_color=arcade.csscolor.WHITE,
                                               caret_color=arcade.csscolor.WHITE)
        
        # Need to call push_handlers of accompanying 
        # window to get text box to react to user. 
        window.push_handlers(self.text_entry)

        return
    
    def draw_text_box(self):
        """
        Draws text box used for user move entry. Intended to 
        be called in accompanying window on_draw() method.

        Args:
            None

        Returns:
            None       
        """
        self.text_batch.draw()
        return