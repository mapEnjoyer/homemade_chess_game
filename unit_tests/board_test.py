"""
File name: board_test.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 08/06/26

@brief: 
    This file contains unit tests for the methods/function in board.py
"""

from visuals import window
from pieces import piece, pawn, rook, knight, bishop, queen, king
from pathlib import Path
import arcade
import constants
import pytest

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
    # Game window to test on
    game_window = window.GameView(is_visible=False)

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

def test_move_handle_invalid_piece_type():
    """
    Test trying to make a move with an invalid piece type.
    """
    # Game window to test on
    game_window = window.GameView(is_visible=False)

    # Try making a pawn move with a piece type that isn't valid
    assert game_window.chess_board.handle_move(piece_type=None,
                                               start_space='E2',
                                               next_space='E4',
                                               player_turn=constants.PlayerColor.WHITE) is False

def test_move_handle_invalid_start_square():
    """
    Test trying to make a move with an invalid starting square.
    """
    # Game window to test on
    game_window = window.GameView(is_visible=False)

    # Try making a pawn move with a start square that isn't valid
    assert game_window.chess_board.handle_move(piece_type=pawn.Pawn,
                                               start_space='I2',
                                               next_space='E4',
                                               player_turn=constants.PlayerColor.WHITE) is False

def test_move_handle_invalid_end_square():
    """
    Test trying to make a move with an invalid ending square.
    """
    # Game window to test on
    game_window = window.GameView(is_visible=False)

    # Try making a pawn move with an end square that isn't valid
    assert game_window.chess_board.handle_move(piece_type=pawn.Pawn,
                                               start_space='E2',
                                               next_space='I4',
                                               player_turn=constants.PlayerColor.WHITE) is False

def test_move_handle_no_piece_on_square():
    """
    Test trying to make a move on a square with no piece.
    """
    # Game window to test on
    game_window = window.GameView(is_visible=False)

    # Try making a pawn move on a square with no piece
    assert game_window.chess_board.handle_move(piece_type=pawn.Pawn,
                                               start_space='E3',
                                               next_space='E4',
                                               player_turn=constants.PlayerColor.WHITE) is False

def test_move_handle_wrong_piece_type():
    """
    Test trying to move a piece with the wrong piece type
    """
    # Game window to test on
    game_window = window.GameView(is_visible=False)

    # Try making a pawn move with the piece type set to bishop
    assert game_window.chess_board.handle_move(piece_type=bishop.Bishop,
                                               start_space='E2',
                                               next_space='E4',
                                               player_turn=constants.PlayerColor.WHITE) is False

def test_move_handle_wrong_color_piece():
    """
    Test trying to move a piece of the wrong color
    """
    # Game window to test on
    game_window = window.GameView(is_visible=False)

    # Try moving black piece on white turn
    assert game_window.chess_board.handle_move(piece_type=pawn.Pawn,
                                               start_space='E7',
                                               next_space='E5',
                                               player_turn=constants.PlayerColor.WHITE) is False

    # Try moving white piece on black turn
    game_window.move_parser.player_turn = constants.PlayerColor.BLACK
    assert game_window.chess_board.handle_move(piece_type=pawn.Pawn,
                                               start_space='E2',
                                               next_space='E4',
                                               player_turn=constants.PlayerColor.BLACK) is False

@pytest.mark.parametrize('col', constants.board_col_labels)
def test_pawn_move_1_space_forward(col):
    """
    Test moving a white pawn and a black pawn "forward" one space
    """
    # Game window to test on
    game_window = window.GameView(is_visible=False)

    # Set white and black spaces
    white_start_space = col + str(2)
    white_end_space = col + str(3)
    black_start_space = col + str(7)
    black_end_space = col + str(6)

    # Move white E2 pawn to E3
    assert game_window.chess_board.handle_move(pawn.Pawn,
                                               start_space=white_start_space,
                                               next_space=white_end_space,
                                               player_turn=constants.PlayerColor.WHITE) is True

    # Check that starting space is empty and ending space is occupied
    assert game_window.chess_board.board_spaces[white_start_space].occupying_piece is None
    assert isinstance(game_window.chess_board.board_spaces[white_end_space].occupying_piece, pawn.Pawn)

    # Move black E7 pawn to E6
    assert game_window.chess_board.handle_move(pawn.Pawn,
                                               start_space=black_start_space,
                                               next_space=black_end_space,
                                               player_turn=constants.PlayerColor.BLACK) is True

    # Check that starting space is empty and ending space is occupied
    assert game_window.chess_board.board_spaces[black_start_space].occupying_piece is None
    assert isinstance(game_window.chess_board.board_spaces[black_end_space].occupying_piece, pawn.Pawn)

@pytest.mark.parametrize('col', constants.board_col_labels)
def test_pawn_move_2_space_forward(col):
    """
    Test moving a white pawn and a black pawn "forward" one space
    """
    # Game window to test on
    game_window = window.GameView(is_visible=False)

    # Set white and black spaces
    white_start_space = col + str(2)
    white_end_space = col + str(4)
    black_start_space = col + str(7)
    black_end_space = col + str(5)

    # Move white E2 pawn to E3
    assert game_window.chess_board.handle_move(pawn.Pawn,
                                               start_space=white_start_space,
                                               next_space=white_end_space,
                                               player_turn=constants.PlayerColor.WHITE) is True

    # Check that starting space is empty and ending space is occupied
    assert game_window.chess_board.board_spaces[white_start_space].occupying_piece is None
    assert isinstance(game_window.chess_board.board_spaces[white_end_space].occupying_piece, pawn.Pawn)

    # Move black E7 pawn to E6
    assert game_window.chess_board.handle_move(pawn.Pawn,
                                               start_space=black_start_space,
                                               next_space=black_end_space,
                                               player_turn=constants.PlayerColor.BLACK) is True

    # Check that starting space is empty and ending space is occupied
    assert game_window.chess_board.board_spaces[black_start_space].occupying_piece is None
    assert isinstance(game_window.chess_board.board_spaces[black_end_space].occupying_piece, pawn.Pawn)

def test_pawn_capture_A_side():
    """
    test both white and black pawns capturing towards A side
    """
    # Game window to test on
    game_window = window.GameView(is_visible=False)

    white_pawn_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.white_pawn_image_name)
    black_pawn_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.black_pawn_image_name)
    white_king_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.white_king_image_name)
    black_king_path = str(Path(__file__).parent.parent / "visuals//textures" / constants.black_king_image_name)

    # Clear all pieces except those needed in test:
    # White pawns on D4, E4
    # Black pawns on D5, E5
    # White king on E1
    # Black king on E8
    game_window.chess_board.pieces = []
    game_window.chess_board.sprite_list = []
    game_window.chess_board.pieces.append(pawn.Pawn(game_window.chess_board.board_spaces['D4'], 
                                                    white_pawn_path, 
                                                    constants.pawn_image_width, 
                                                    constants.PlayerColor.WHITE))
    game_window.chess_board.pieces.append(pawn.Pawn(game_window.chess_board.board_spaces['E4'], 
                                                    white_pawn_path, 
                                                    constants.pawn_image_width, 
                                                    constants.PlayerColor.WHITE))
    game_window.chess_board.pieces.append(pawn.Pawn(game_window.chess_board.board_spaces['D5'], 
                                                    black_pawn_path, 
                                                    constants.pawn_image_width, 
                                                    constants.PlayerColor.BLACK))
    game_window.chess_board.pieces.append(pawn.Pawn(game_window.chess_board.board_spaces['E5'], 
                                                    black_pawn_path, 
                                                    constants.pawn_image_width, 
                                                    constants.PlayerColor.BLACK))
    game_window.chess_board.pieces.append(king.King(game_window.chess_board.board_spaces['E1'],
                                                    white_king_path,
                                                    constants.king_image_width,
                                                    constants.PlayerColor.WHITE))
    game_window.chess_board.pieces.append(king.King(game_window.chess_board.board_spaces['E8'],
                                                    black_king_path,
                                                    constants.king_image_width,
                                                    constants.PlayerColor.BLACK))

    for piece in game_window.chess_board.pieces:
        # Add sprite back to sprite list
        game_window.chess_board.sprite_list.append(piece.sprite)

    # White pawn on D4 captures black pawn on E5
    assert game_window.chess_board.handle_move(pawn.Pawn, 'E4', 'D5', constants.PlayerColor.WHITE) is True
    assert game_window.chess_board.board_spaces['E4'].occupying_piece is None
    assert isinstance(game_window.chess_board.board_spaces['D5'].occupying_piece, pawn.Pawn)
    assert game_window.chess_board.board_spaces['D5'].occupying_piece.color == constants.PlayerColor.WHITE

    # Black pawn on D5 captures white pawn on E4
    
    
