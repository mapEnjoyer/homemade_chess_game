"""
File name: window.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains the necessary classes, functions, methods, etc.for
    creating and maintaining the window settings for the chess game.  
"""
import arcade
import constants
from pathlib import Path
from visuals import board, move_parser

class GameView(arcade.Window):
    """
    Main application class. Handles visuals for the game

    Attributes:
        - prev_width: Width of the screen when it was last drawn
        - prev_height: Height of the screen when it was last drawn
        - background_color: Color of the background
        - chess_board: Chess board object to display in window
        - move_parser: Handler for user controlled piece movement
    """

    def __init__(self):
        """
        Initializes the game window by performing the following steps:
            - Creates the window
            - Initializes the saved prev_width/prev_height
            - Sets the background color
            - Initializes the chess board
            - Initializes the move parser used for move entry
            - Runs setup

        Args:
            None

        Returns:
            None  
        """

        # Call the parent class to set up the window
        # TODO: Probably want to save these settings in a user_config.json 
        super().__init__(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT, constants.WINDOW_TITLE, resizable=True)

        # Initialize "previous" screen sizes. Used for determining if 
        # screen size has changed and position values need calculated
        self.prev_width  = constants.WINDOW_WIDTH
        self.prev_height = constants.WINDOW_HEIGHT

        # Set window settings
        self.background_color = arcade.csscolor.DARK_OLIVE_GREEN # Background color

        # Chess board object
        self.chess_board = board.Board()

        # Create move parser
        self.move_parser = move_parser.MoveParser(self)

        # Run setup
        self.setup()

        return

    def setup(self):
        """
        Set up the game here. Call this function to restart the game.
        
        Args:
            None

        Returns:
            None
        """
        # Update positions of all objects drawn on screen
        self.__update_screen_positions()
        
        return

    def on_draw(self):
        """
        Render the screen. Screen rendering requires updating positions of
        on screen objects BEFORE drawing. Positions are always updated whenever
        the size of the screen has changed from the last pass.

        Args:
            None

        Returns:
            None
        """

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here

        if min(self.prev_height, self.prev_width) != min(self.height, self.width):
            # Screen size has changed, update positions of all on screen objects
            self.__update_screen_positions()

        # Save screen size for next pass
        self.prev_height = self.height
        self.prev_width  = self.width

        if all(val is not None for val in [self.move_parser.piece_type, self.move_parser.cur_space, self.move_parser.new_space]):
            # Player move was input into move parser. Pass along to board
            if self.chess_board.handle_move(self.move_parser.piece_type, 
                                            self.move_parser.cur_space, 
                                            self.move_parser.new_space,
                                            self.move_parser.player_turn):
            
                # Update player turn based on if move was handled successfully
                if self.move_parser.player_turn == constants.PlayerColor.WHITE:
                     self.move_parser.player_turn = constants.PlayerColor.BLACK
                else:
                     self.move_parser.player_turn = constants.PlayerColor.WHITE
    
            # Clear move parser after move is handled
            self.move_parser.piece_type = self.move_parser.cur_space = self.move_parser.new_space = None


        # Draw the chess board
        self.chess_board.draw_board()

        # Draw the text box via the batch
        self.move_parser.draw_text_box()
        return

    def __update_screen_positions(self):
        """ 
            Updates all positions of objects drawn on screen. 
            Intended to be called whenever screen size changes
        Args:
            None

        Returns:
            None
        """
        # Update checkerboard positions
        self.__update_board_positions()

        return

    def __update_board_positions(self):
        """
            Updates all positions of the checkerboard squares,
            row labels, column labels, piece sprites and move _x
            parser text box. This is done by allocating a 12x12 
            grid worth of squares in space starting at the bottom 
            left hand corner of the screen. Position data is assigned 
            to each of the chess board squares and labels to have 
            them appear on the screen in the proper location. A 2x2 
            square border is alloted at the edges of the board to 
            give a margin.

        Args:
            None

        Returns:
            None
        """

        # Scale the square size relative to the window
        # Chess board requires 8x8 squares, we use a factor of 1/12th to give margins
        square_size = min(self.width, self.height)/12
    
        # Set staring X/Y coordinates (center of square x = 2, y = 2 on our imaginary 12x12 grid)
        y_start = x_pos = y_pos = square_size * 2.5

        for space in self.chess_board.board_spaces:
            # Update row count
            row_count = int(space[-1])

            # Update space positions relative to window size
            self.chess_board.board_spaces[space].center_x = x_pos
            self.chess_board.board_spaces[space].center_y = y_pos
            self.chess_board.board_spaces[space].length   = square_size

            if row_count != 8:
                # Still in the same columnm. Increment the y position
                y_pos += square_size
            else:
                # Shifting over to the next column. Reset y position and shift x
                y_pos = y_start
                x_pos += square_size

        # After space positions are determined, piece sprite locations need updated to match those square locations
        # To do this, call the update_space method of each piece using the square it's already in
        for piece in self.chess_board.pieces:
            piece.update_space(piece.occupied_square)          

        # Determine row/column label font size (1/4th square size seemed good from testing)
        font_size = square_size / 4 

        # Calculate text shift (used to center label along the square)    
        text_shift = font_size / 2

        # Update the column label x/y positions and font size
        for col in constants.board_col_labels:
            # Column label x position is the same as the square above it shifted by the text_shift
            self.chess_board.col_labels[col].x = self.chess_board.board_spaces[col+"1"].center_x - text_shift

            # Column label y position is 1 square below the first 1
            self.chess_board.col_labels[col].y = self.chess_board.board_spaces[col+"1"].center_y - square_size
            self.chess_board.col_labels[col].font_size = font_size
        
        # Update the row label x/y positions
        for row in constants.board_row_labels:
            # Row label x position is position is 1 square to  the left of first column 1
            self.chess_board.row_labels[row].x = self.chess_board.board_spaces["A"+row].center_x - square_size
            
            # Row label y position is same as the square to the right shifted by the text shift
            self.chess_board.row_labels[row].y = self.chess_board.board_spaces["A"+row].center_y - text_shift
            self.chess_board.row_labels[row].font_size = font_size 

        # Update the move parser text box size and location
        # Move parser x location should start at last square
        self.move_parser.text_entry.x = x_pos

        # Move parser y location should be in line with row 1 of chess board
        self.move_parser.text_entry.y = y_start

        # Move parser width should always be 1/4th of window size
        self.move_parser.text_entry.width =  self.width/4 

        return

