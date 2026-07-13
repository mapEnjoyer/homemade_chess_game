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
import constants
import excpetions
from pieces import pawn, rook, knight, bishop, queen, king

class MoveParser():
    """
    Move parser class. Used to handle text input (and eventually mouse inputs)
    for players to move pieces around the chess board.

    Attributes:
        text_batch: Graphics batch the move parser widget is apart of. 
        text_entry: Widget type the parser is apart of. 
        piece_type: Type of piece to be moved next. Will be 'None' if no move is to be processed.
        cur_space: Space next move is starting from. Will be 'None' if no move is to be processed.
        new_space: Space next move is moving to. Will be 'None' if no move is to be processed.
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
        # Initialize attributes
        self.piece_type = None
        self.cur_space = None
        self.new_space = None

        # Text entry window
        # The only way I could find to get the text box widget
        # to appear on screen was to make it apart of a "batch" 
        # and call the batch.draw() method on each frame.
        self.text_batch = pyglet.graphics.Batch()

        # x, y and width does not matter as the window will have 
        # to reassign these settings based on the size of the window.
        self.text_entry = pyglet.gui.TextEntry(text="", 
                                               x=0, 
                                               y=0, 
                                               width=300, 
                                               batch=self.text_batch, 
                                               color=arcade.csscolor.BLACK, 
                                               text_color=arcade.csscolor.WHITE,
                                               caret_color=arcade.csscolor.WHITE)
        
        # Set "on_commit" handler to method used for text entry
        self.text_entry.on_commit = self.parse_move_entry

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
    
    def parse_move_entry(self, widget: pyglet.gui.TextEntry, text: str):
        """
        Takes in move string and sends information to board regarding 
        which piece type is being move and where it is trying to go. It
        expects a string that uses a modified version of standard chess
        algebraic notation. Valid string lengths will either be 4 or 5
        characters, depending on if the piece is a pawn. 
        
        Examples:
            - Pawn on E2 -> E4: E2E4
            - Knight on B1 -> C3: KB1C3

        This method is called whenever the user hits "enter" on the move
        entry text box.

        Args:
            None

        Returns:
            None          
        """

        # Remove all white space from text
        text = " ".join(text.split())

        # Convert to upper case
        text = text.upper()

        try:
            if len(text) == 4:
                # Assume piece is of type 'pawn' as pawn moves do not 
                # include the piece type in algebraic notation (ex: e4)
                piece_type = pawn.Pawn

            elif len(text) == 5:

                if text[0] == 'R':
                    # Piece is of type 'rook'
                    piece_type = rook.Rook

                elif text[0] == 'N':
                    # Piece is of type 'knight'
                    piece_type = knight.Knight

                elif text[0] == 'B':
                    # Piece is of type 'bishop'
                    piece_type = bishop.Bishop

                elif text[0] == 'Q':
                    # Piece is of type 'queen'
                    piece_type = queen.Queen

                elif text[0] == 'K':
                    # Piece is of type 'king'
                    piece_type = king.King

                else:
                    # Invalid move entry, notify
                    raise excpetions.InvalidPieceTypeError()
                
            else:
                # Move input too long. Raise exception
                raise InvalidMoveEntry()

                
            # Now that we have determined piece type, attempt to determine current and new squares
            cur_space = text[-4:-2]
            new_space = text[-2:]

            if any(space not in constants.space_names for space in [cur_space, new_space]):
                raise excpetions.InvalidSpaceError()

        except excpetions.InvalidPieceTypeError: 
            # TODO: Show error message in game screen, not terminal
            print (f'Invalid piece type! Valid piece types include "R":Rook, "N":Knight, "B":Bishop, "Q":Queen, "K":King. Pawn moves do not include a "P" (ex: E4).')

        except excpetions.InvalidSpaceError:
            # TODO: Show error message in game screen, not terminal
            print (f'Space does not exist on board! Use the row/column labels to determine square piece is moving to. Column letter always comes before row number (ex: E4).')

        except InvalidMoveEntry:
            # TODO: Show error message in game screen, not terminal
            print (f'Move entry is invalid. Length of move should be no longer than 3 characters (ex: KC3)')

        else:
            # Assign piece type and space to move parser so they can be used by the window
            self.piece_type = piece_type
            self.cur_space = cur_space
            self.new_space = new_space

        finally:
            # Clear text box after parsing is complete
            self.text_entry._doc.text = ""

        return

class InvalidMoveEntry(Exception):
    """
    Custom exception handler for when a move is invalid for reasons other than 
    invalid piece type or space reference.
    """
    
    def __init__(self):

        """
        Notifies the player that the move they have entered is invalid for reasons 
        other than invalid piece type or space reference.

        Args:
            None

        Returns:
            None
        """
        super().__init__()