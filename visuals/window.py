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
from pathlib import Path
from visuals import board

# Window Constants
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_TITLE = "EAK's Chess Game"

# Chess board object
chess_board = board.board()

class GameView(arcade.Window):
    """
    Main application class. Handles visuals for the game
    """

    def __init__(self):

        # Call the parent class to set up the window
        # TODO: Probably want to save these settings in a user_config.json 
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)

        # Initialize "previous" screen sizes. Used for determining if 
        # screen size has changed and position values need calculated
        self.prev_width  = WINDOW_WIDTH
        self.prev_height = WINDOW_HEIGHT

        # Set window settings
        self.background_color = arcade.csscolor.DARK_OLIVE_GREEN # Background color

        # Set path to visuals
        visuals_path = Path.cwd()._str + '/visuals'

        # TODO: Load textures and sprites

        return

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Update positions of all objects drawn on screen
        self.__update_screen_positions()
        pass

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here

        if self.prev_height != self.height or self.prev_width != self.width:
            # Screen size has changed, update positions of all on screen objects
            self.__update_screen_positions()

        # Save screen size for next pass
        self.prev_height = self.height
        self.prev_width  = self.width

        # Draw the chess board
        chess_board.draw_board()
        return

    def __update_screen_positions(self):
        """ 
            Updates all positions of objects drawn on screen. 
            Intended to be called whenever screen size changes 
        """
        # Update checkerboard positions
        self.__update_board_positions()

        return

    def __update_board_positions(self):
        """
            Updates all positions of the checkerboard squares.
        """

        # Scale the square size relative to the window
        # Chess board requires 8x8 squares, we use a factor of 1/12th to give margins
        if self.width <= self.height:
            square_size = self.width/12 
        else:
            square_size = self.height/12
    
        # Set staring X/Y coordinates
        x_pos = y_pos = square_size * 2.5

        for space in chess_board.board_spaces:
            # Update  row count
            row_count = int(space[1])

            # Update space positions relative to window size
            chess_board.board_spaces[space].center_x = x_pos
            chess_board.board_spaces[space].center_y = y_pos
            chess_board.board_spaces[space].length   = square_size

            if row_count != 8:
                # Still in the same columnm. Increment the y position
                y_pos += square_size
            else:
                # Shifting over to the next column. Reset y position and shift x
                y_pos = square_size * 2.5
                x_pos += square_size

        # Determine row/column label font size (1/4th square size seemed good from testing)
        font_size = square_size / 4      
    
        # Update the column label x/y positions and font size
        for col in board.board_col_labels:
            chess_board.col_labels[col].x         = chess_board.board_spaces[col+"1"].center_x - font_size/2
            chess_board.col_labels[col].y         = chess_board.board_spaces[col+"1"].center_y - square_size
            chess_board.col_labels[col].font_size = font_size
        # Update the row label x/y positions
        for row in board.board_row_labels:
            chess_board.row_labels[row].x         = chess_board.board_spaces["A"+row].center_x - square_size
            chess_board.row_labels[row].y         = chess_board.board_spaces["A"+row].center_y - font_size/2       
            chess_board.row_labels[row].font_size = font_size      

        return
    
"""
Function Name: window_init

    Initializes the window containing game visuals

@param  None
@return None
"""
def window_init():
    # Create a instance of the GameView class
    window = GameView()
    window.setup()

    return

