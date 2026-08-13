"""
File name: board_test.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 08/06/26

@brief: 
    This file contains unit tests for the methods/function in board.py
"""

from visuals import window
from pieces import piece as piece
import arcade
import constants
import pytest

# Game window to test on
game_window = window.GameView(is_visible=False)

#TODO: Test will need updated if we add different colored themes
@pytest.mark.parametrize('square_color_1', [arcade.color.BISTRE])
@pytest.mark.parametrize('square_color_2', [arcade.color.TAN])
@pytest.mark.parametrize('piece_color_1', [constants.PlayerColor.WHITE])
@pytest.mark.parametrize('piece_color_2', [constants.PlayerColor.BLACK])
def test_board_init(square_color_1:arcade.color, 
                    square_color_2:arcade.color, 
                    piece_color_1:constants.PlayerColor, 
                    piece_color_2:constants.PlayerColor):
    """
    Test that the board is initialized properly with the following conditions:
        - 64 squares: 32 one color, 32 another
        - 16 pieces of one color (8 pawns, 2 rooks, 2 knights, 2 bishops, 1 queen, 1 king)
        - 16 pieces of another color (8 pawns, 2 rooks, 2 knights, 2 bishops, 1 queen, 1 king)
        - 32 sprites
        - column label text (A-H)
        - row label text (1-8)
    """
    # Start by check squares
    color_1_count = 0
    color_2_count = 0
    for square in game_window.chess_board.board_spaces:
        # Make sure it's actually a board square
        assert isinstance(game_window.chess_board.board_spaces[square], piece.Board_Space)

        if game_window.chess_board.board_spaces[square].color == square_color_1:
            color_1_count+=1

        elif game_window.chess_board.board_spaces[square].color == square_color_2:
            color_2_count+=1

    # Total square count should be 64, with 32 of each color
    assert len(game_window.chess_board.board_spaces) == 64
    assert color_1_count == 32
    assert color_2_count == 32

    # Check pieces
    color_1_count = 0
    color_2_count = 0

    for chess_piece in game_window.chess_board.pieces:
        # Make sure it's a piece
        assert isinstance(chess_piece, piece.Piece)
        if chess_piece.color == piece_color_1:
            color_1_count+=1

        elif chess_piece.color == piece_color_2:
            color_2_count+=1

    # Total piece count should be 32, 16 of each color
    assert len(game_window.chess_board.pieces) == 32
    assert color_1_count == 16
    assert color_2_count == 16

    # Check row labels
    for label in game_window.chess_board.row_labels:
        assert isinstance(game_window.chess_board.row_labels[label], arcade.Text)
    assert len(game_window.chess_board.row_labels) == 8

    # Check column labels
    for label in game_window.chess_board.col_labels:
        assert isinstance(game_window.chess_board.col_labels[label], arcade.Text)
    assert len(game_window.chess_board.col_labels) == 8
