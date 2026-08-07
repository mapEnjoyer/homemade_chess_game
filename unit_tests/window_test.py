"""
File name: window_test.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 08/06/26

@brief: 
    This file contains unit tests for the methods/function in window.py
"""

from visuals import window
import pytest

# Game window to test on
game_window = window.GameView()

def test_init_window():
    """
    test initializing window
    """
    assert game_window is not None
