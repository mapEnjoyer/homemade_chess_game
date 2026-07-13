"""
File name: board.py
Project: homemade_chess_game
Author: Eric Kellmyer
Date: 05/30/26

@brief: 
    This file contains the necessary classes, functions, methods, etc.
    maintaining the checkerboard pattern of the chess game.
"""

import arcade
import constants
from pieces import piece, pawn, rook, knight, bishop, queen, king
from pathlib import Path
class Board():
    """
    Board class. Used to access all spaces on the board.

    Attributes:
        - board_spaces: Dictionary containing all 64 board space objects
        - col_labels: Dictonary containing 8 column label text objects
        - row_labels: Dictionary containing 8 row label text objects
        - white_pieces: List of all white pieces currently on the board. As pieces are removed, they are popped from the list.
        - black_pieces: List of all black pieces currently on the board. As pieces are removed, they are popped from the list.
    """

    def __init__(self):
        """
        Initializes the board object by creating the board spaces, row and 
        column dictionaries and populating them with their necessary objects.
        
        Args:
            None

        Returns:
            None    
        """

        # Dictonary containing all board spaces.
        # {"A1" : piece.Board_Space A1; "A2": piece.Board_Space A2; ...}
        self.board_spaces:dict[str, piece.Board_Space] = {}

        # Dictionary containing all column label text objects
        # {"A": Text A; "B": Text B; ...}
        self.col_labels:dict[str, arcade.Text] = {}

        # Dictionary containing all row label text objects
        # {"1": Text 1; "2": Text 2; ...}
        self.row_labels:dict[str, arcade.Text] = {}

        # List containing all white pieces on board
        self.white_pieces = []

        # List containing all black pieces on board
        self.black_pieces = []

        # Sprite list containing all sprites on the board
        self.sprite_list = arcade.SpriteList()

        # Initialize chess board squares
        self.__init_squares()

        # Initialize the chess board labels
        self.__init_labels()

        # Initialize white pieces
        self.__init_white_pieces()

        # TODO: Init black pieces
        self.__init_black_pieces()

        return

    def __init_squares(self):
        """
        Initializes the board squares by creating the object, populating the board_spaces 
        dictionary and assigning the space color. It does NOT assign their x/y positions 
        as it is up to the window to do so.

        Args: 
            None

        Returns:
            None          
        """

        # A1 is brown on chess board
        space_color = arcade.color.BISTRE
        row_count = 0

        for name in constants.space_names:
            
            # Update row_count 
            row_count = int(name[-1])

            # Create a space class for each space
            self.board_spaces[name] = piece.Board_Space(color = space_color, name=name)

            if row_count != 8:
                if space_color == arcade.color.BISTRE:
                    # Swap color to tan
                    space_color = arcade.color.TAN

                else:
                    # Swap color back to black
                    space_color = arcade.color.BISTRE

        return

    def __init_labels(self):
        """
        Initializes the board labels by creating the object, assigning it to the dictionary and 
        setting the color to black. It does NOT assign their x/y positions as it is up to the 
        window to do so.

        Args: 
            None

        Returns:
            None 
        """
        for row in constants.board_row_labels:
            # Create text objects for each row lable
            # Don't worry about text position, its up
            # to the window to set the positions before drawing
            self.row_labels[row] = arcade.Text(text=row, x = 0, y = 0, color=arcade.color.BLACK, align="center")

        for col in constants.board_col_labels:
            # Create text objects for each row lable
            # Don't worry about text position, its up
            # to the window to set the positions before drawing
            self.col_labels[col] = arcade.Text(text=col, x = 0, y = 0, color=arcade.color.BLACK, align="center")

        return
    
    def __init_white_pieces(self):
        """
        Initializes the white pieces by creating objects for each piece inside the associated piece list.

        Args: 
            None

        Returns:
            None         
        """
        # Create the A2-H2 pawns
        text_file_path = Path(__file__).parent / "textures" / constants.white_pawn_image_name
        
        self.white_pieces.append(pawn.Pawn(self.board_spaces["A2"], text_file_path.__str__(), constants.pawn_image_width))
        self.white_pieces.append(pawn.Pawn(self.board_spaces["B2"], text_file_path.__str__(), constants.pawn_image_width))
        self.white_pieces.append(pawn.Pawn(self.board_spaces["C2"], text_file_path.__str__(), constants.pawn_image_width))
        self.white_pieces.append(pawn.Pawn(self.board_spaces["D2"], text_file_path.__str__(), constants.pawn_image_width))
        self.white_pieces.append(pawn.Pawn(self.board_spaces["E2"], text_file_path.__str__(), constants.pawn_image_width))
        self.white_pieces.append(pawn.Pawn(self.board_spaces["F2"], text_file_path.__str__(), constants.pawn_image_width))
        self.white_pieces.append(pawn.Pawn(self.board_spaces["G2"], text_file_path.__str__(), constants.pawn_image_width))
        self.white_pieces.append(pawn.Pawn(self.board_spaces["H2"], text_file_path.__str__(), constants.pawn_image_width))

        # Create A1/H1 rooks
        text_file_path = Path(__file__).parent / "textures" / constants.white_rook_image_name

        self.white_pieces.append(rook.Rook(self.board_spaces["A1"], text_file_path.__str__(), constants.rook_image_width))
        self.white_pieces.append(rook.Rook(self.board_spaces["H1"], text_file_path.__str__(), constants.rook_image_width))

        # Create B1/G1 knights
        text_file_path = Path(__file__).parent / "textures" / constants.white_knight_image_name

        self.white_pieces.append(knight.Knight(self.board_spaces["B1"], text_file_path.__str__(), constants.knight_image_width))
        self.white_pieces.append(knight.Knight(self.board_spaces["G1"], text_file_path.__str__(), constants.knight_image_width))

        # Create C1/F1 bishops
        text_file_path = Path(__file__).parent / "textures" / constants.white_bishop_image_name

        self.white_pieces.append(bishop.Bishop(self.board_spaces["C1"], text_file_path.__str__(), constants.bishop_image_width))
        self.white_pieces.append(bishop.Bishop(self.board_spaces["F1"], text_file_path.__str__(), constants.bishop_image_width))

        # Create D1 queen
        text_file_path = Path(__file__).parent / "textures" / constants.white_queen_image_name

        self.white_pieces.append(queen.Queen(self.board_spaces["D1"], text_file_path.__str__(), constants.queen_image_width))

        # Create E1 king
        text_file_path = Path(__file__).parent / "textures" / constants.white_king_image_name

        self.white_pieces.append(king.King(self.board_spaces["E1"], text_file_path.__str__(), constants.king_image_width))

        # After each piece is created, add its sprite to the sprite list so they can be drawn each frame
        for piece in self.white_pieces:
            self.sprite_list.append(piece.sprite)

        return
    
    def __init_black_pieces(self):
        """
        Initializes the black pieces by creating objects for each piece inside the associated piece list.

        Args: 
            None

        Returns:
            None         
        """
        # Create the A7-H7 pawns
        text_file_path = Path(__file__).parent / "textures" / constants.black_pawn_image_name

        self.black_pieces.append(pawn.Pawn(self.board_spaces["A7"], text_file_path.__str__(), constants.pawn_image_width))
        self.black_pieces.append(pawn.Pawn(self.board_spaces["B7"], text_file_path.__str__(), constants.pawn_image_width))
        self.black_pieces.append(pawn.Pawn(self.board_spaces["C7"], text_file_path.__str__(), constants.pawn_image_width))
        self.black_pieces.append(pawn.Pawn(self.board_spaces["D7"], text_file_path.__str__(), constants.pawn_image_width))
        self.black_pieces.append(pawn.Pawn(self.board_spaces["E7"], text_file_path.__str__(), constants.pawn_image_width))
        self.black_pieces.append(pawn.Pawn(self.board_spaces["F7"], text_file_path.__str__(), constants.pawn_image_width))
        self.black_pieces.append(pawn.Pawn(self.board_spaces["G7"], text_file_path.__str__(), constants.pawn_image_width))
        self.black_pieces.append(pawn.Pawn(self.board_spaces["H7"], text_file_path.__str__(), constants.pawn_image_width))

        # Create A8/H8 rooks
        text_file_path = Path(__file__).parent / "textures" / constants.black_rook_image_name

        self.black_pieces.append(rook.Rook(self.board_spaces["A8"], text_file_path.__str__(), constants.rook_image_width))
        self.black_pieces.append(rook.Rook(self.board_spaces["H8"], text_file_path.__str__(), constants.rook_image_width))

        # Create B8/G8 knights
        text_file_path = Path(__file__).parent / "textures" / constants.black_knight_image_name

        self.black_pieces.append(knight.Knight(self.board_spaces["B8"], text_file_path.__str__(), constants.knight_image_width))
        self.black_pieces.append(knight.Knight(self.board_spaces["G8"], text_file_path.__str__(), constants.knight_image_width))

        # Create C8/F8 bishops
        text_file_path = Path(__file__).parent / "textures" / constants.black_bishop_image_name

        self.black_pieces.append(bishop.Bishop(self.board_spaces["C8"], text_file_path.__str__(), constants.bishop_image_width))
        self.black_pieces.append(bishop.Bishop(self.board_spaces["F8"], text_file_path.__str__(), constants.bishop_image_width))   

        # Create D8 queen
        text_file_path = Path(__file__).parent / "textures" / constants.black_queen_image_name

        self.black_pieces.append(queen.Queen(self.board_spaces["D8"], text_file_path.__str__(), constants.queen_image_width))

        # Create E8 king
        text_file_path = Path(__file__).parent / "textures" / constants.black_king_image_name
        
        self.black_pieces.append(king.King(self.board_spaces["E8"], text_file_path.__str__(), constants.king_image_width))        

        # After each piece is created, add its sprite to the sprite list so they can be drawn each frame
        for piece in self.black_pieces:
            self.sprite_list.append(piece.sprite)

        return
    
    def draw_board(self):
        """ 
        Draws the chess board on screen by drawing each square,
        row and column label based on set positions.

        Args: 
            None

        Returns:
            None    
        """
        for space in self.board_spaces:
            # Draw the square on the screen
            self.board_spaces[space].draw_square()

        # Draw the column labels
        for col in self.col_labels:
            self.col_labels[col].draw()

        # Draw the row labels
        for row in self.row_labels:
            self.row_labels[row].draw()

        # Draw the pieces
        self.sprite_list.draw()

        return
    
    def handle_move(self, piece_type, start_space:str, next_space:str, player_turn:constants.PlayerColor):
        """
        Handles incoming move by first determining if move is possible. If so,
        the piece is moved to that square, resolving any captures at the destination.

        Args: 
            piece_type: type of piece being moved. Valid piece tpyes include:
                - Pawn
                - Rook
                - Knight
                - Bishop
                - Queen
                - King

            start_space: space to start from. Space must match one of the spaces found in constants.space_names
            next_space: space to move to. Space must match one of the spaces found in constants.space_names

        Returns:
            piece_moved: Boolean indicator True if piece moved, False otherwise   
        """
        piece_moved = False
        
        try:
            # Check that piece type is valid
            if piece_type not in constants.valid_piece_types:
                # TODO: raise exception
                raise Exception                


            # Check that starting square is valid
            if start_space not in constants.space_names:
                # TODO: raise exception
                raise Exception

            # Check that next square is valid
            if next_space not in constants.space_names:
                # TODO: raise exception
                raise Exception

            # Check that the piece being moved is the right color
            if self.board_spaces[start_space].occupying_piece.color != player_turn:
                # TODO: raise exception
                raise Exception

            # Run move handler for the piece type
            match(type(self.board_spaces[start_space].occupying_piece)):
                case pawn.Pawn:
                    # Run pawn handler
                    piece_moved = self.__pawn_move_handler(self.board_spaces[start_space].occupying_piece, next_space, player_turn)
                    pass
                case _:
                    pass

        except:
            pass

        return piece_moved

    def __pawn_move_handler(self, pawn:pawn.Pawn, next_space:str, player_turn:constants.PlayerColor):
        """
        Handles pawn moves by first checking if the move between the spaces is
        technically viable per how the pawn moves. If so, then any spaces the 
        pawn would pass through are checked for obstacles if moving forward. If
        the pawn is moving diagonally, then that space is checked for a piece of
        the opposing color.

        Args:
            pawn: Pawn object being moved.
            next_space: space to move to. Space must match one of the spaces found in constants.space_names

        Returns:
            pawn_moved: Boolean True if pawn moved, False otherwise  
        """
        pawn_moved = False

        try:
            # Run move validity check at the piece level
            move_is_valid = pawn.is_move_valid(next_space)

            if move_is_valid:

                # Determine direction value based on color
                if player_turn == constants.PlayerColor.WHITE:
                    direction = 1 # positive means "forward" is incrementing row count
                else:
                    direction = -1 # negative means "forward" is decrementing row count

                # Move is technically valid. Next steps depend on if pawn is move vertically or diagonally
                cur_col = pawn.occupied_square.name[0]
                cur_row = int(pawn.occupied_square.name[1])
                next_col = next_space[0]
                next_row = int(next_space[1])
                if  cur_col == next_col :
                    # Pawn is staying in the same column. Check square(s) it is moving through.
                    for row in range(cur_row+direction, next_row+direction, direction):
                        if self.board_spaces[cur_col+str(row)].occupying_piece is not None:
                            # TODO: A piece occupies the row(s) ahead of the pawn. Raise an exception
                            raise Exception

                else:
                    # Pawn is moving diagonally. Check destination for opposing color piece
                    if self.board_spaces[next_space].occupying_piece is None \
                    or pawn.color == self.board_spaces[next_space].occupying_piece.color:
                        # TODO: There's no piece to capture. Raise an exception
                        raise Exception


                # No pieces occupying the spaces ahead of the pawn. Move it to the new space
                pawn.update_space(self.board_spaces[next_space])
                pawn_moved = True

        except:
            pass
            
        return pawn_moved

