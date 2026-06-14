"""
File name: constants.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains constants intended to be used throughout the project.
"""

from typing import Final

# List of all board spaces as strings
space_names:Final =  ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                      "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
                      "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8",
                      "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
                      "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8",
                      "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8",
                      "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8",
                      "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8",]

# List of board column labels as strings
board_col_labels:Final = ["A", "B", "C", "D", "E", "F", "G", "H"]

# List of board row labels as strings
board_row_labels:Final = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Window Constants
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_TITLE = "EAK's Chess Game"

# Piece texture image constants
white_pawn_image_name = "white_pawn.png"
white_rook_image_name = "white_rook.png"
white_knight_image_name = "white_knight.png"
white_bishop_image_name = "white_bishop.png"

# Piece image size constants
pawn_image_width = 110
pawn_image_height = 110
rook_image_width = 110
rook_image_height = 110
knight_image_width = 110
knight_image_height = 110
bishop_image_width = 120
bishop_image_height = 125