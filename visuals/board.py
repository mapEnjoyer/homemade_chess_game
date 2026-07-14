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

        # List containing all pieces on board
        self.pieces = []

        # Sprite list containing all sprites on the board
        self.sprite_list = arcade.SpriteList()

        # Initialize chess board squares
        self.__init_squares()

        # Initialize the chess board labels
        self.__init_labels()

        # Initialize white pieces
        self.__init_white_pieces()

        # Initialize black pieces
        self.__init_black_pieces()

        # Initialize sprites
        self.__init_sprites()

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
        
        self.pieces.append(pawn.Pawn(self.board_spaces["A2"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["B2"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["C2"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["D2"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["E2"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["F2"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["G2"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["H2"], text_file_path.__str__(), constants.pawn_image_width))

        # Create A1/H1 rooks
        text_file_path = Path(__file__).parent / "textures" / constants.white_rook_image_name

        self.pieces.append(rook.Rook(self.board_spaces["A1"], text_file_path.__str__(), constants.rook_image_width))
        self.pieces.append(rook.Rook(self.board_spaces["H1"], text_file_path.__str__(), constants.rook_image_width))

        # Create B1/G1 knights
        text_file_path = Path(__file__).parent / "textures" / constants.white_knight_image_name

        self.pieces.append(knight.Knight(self.board_spaces["B1"], text_file_path.__str__(), constants.knight_image_width))
        self.pieces.append(knight.Knight(self.board_spaces["G1"], text_file_path.__str__(), constants.knight_image_width))

        # Create C1/F1 bishops
        text_file_path = Path(__file__).parent / "textures" / constants.white_bishop_image_name

        self.pieces.append(bishop.Bishop(self.board_spaces["C1"], text_file_path.__str__(), constants.bishop_image_width))
        self.pieces.append(bishop.Bishop(self.board_spaces["F1"], text_file_path.__str__(), constants.bishop_image_width))

        # Create D1 queen
        text_file_path = Path(__file__).parent / "textures" / constants.white_queen_image_name

        self.pieces.append(queen.Queen(self.board_spaces["D1"], text_file_path.__str__(), constants.queen_image_width))

        # Create E1 king
        text_file_path = Path(__file__).parent / "textures" / constants.white_king_image_name

        self.pieces.append(king.King(self.board_spaces["E1"], text_file_path.__str__(), constants.king_image_width))

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

        self.pieces.append(pawn.Pawn(self.board_spaces["A7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["B7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["C7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["D7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["E7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["F7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["G7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["H7"], text_file_path.__str__(), constants.pawn_image_width))

        # Create A8/H8 rooks
        text_file_path = Path(__file__).parent / "textures" / constants.black_rook_image_name

        self.pieces.append(rook.Rook(self.board_spaces["A8"], text_file_path.__str__(), constants.rook_image_width))
        self.pieces.append(rook.Rook(self.board_spaces["H8"], text_file_path.__str__(), constants.rook_image_width))

        # Create B8/G8 knights
        text_file_path = Path(__file__).parent / "textures" / constants.black_knight_image_name

        self.pieces.append(knight.Knight(self.board_spaces["B8"], text_file_path.__str__(), constants.knight_image_width))
        self.pieces.append(knight.Knight(self.board_spaces["G8"], text_file_path.__str__(), constants.knight_image_width))

        # Create C8/F8 bishops
        text_file_path = Path(__file__).parent / "textures" / constants.black_bishop_image_name

        self.pieces.append(bishop.Bishop(self.board_spaces["C8"], text_file_path.__str__(), constants.bishop_image_width))
        self.pieces.append(bishop.Bishop(self.board_spaces["F8"], text_file_path.__str__(), constants.bishop_image_width))   

        # Create D8 queen
        text_file_path = Path(__file__).parent / "textures" / constants.black_queen_image_name

        self.pieces.append(queen.Queen(self.board_spaces["D8"], text_file_path.__str__(), constants.queen_image_width))

        # Create E8 king
        text_file_path = Path(__file__).parent / "textures" / constants.black_king_image_name
        
        self.pieces.append(king.King(self.board_spaces["E8"], text_file_path.__str__(), constants.king_image_width))        

        return
    
    def __init_sprites(self):
        """
        Initializes the sprite list by adding all piece sprites to the sprite list.

        Args: 
            None

        Returns:
            None    
        """
        for piece in self.pieces:
            self.sprite_list.append(piece.sprite)

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
                # raise exception indicating the piece type is not valid
                raise InvalidMoveException('Piece type does not exist.')                

            # Check that starting square is valid
            if start_space not in constants.space_names:
                # raise exception indicating the starting space does not exist
                raise InvalidMoveException('Starting space does not exist.')     

            # Check that next square is valid
            if next_space not in constants.space_names:
                # raise exception indicating destination space does not exist
                raise InvalidMoveException('Destination space does not exist.')     
            
            # Set piece we are working with
            piece = self.board_spaces[start_space].occupying_piece

            # Check that the piece being moved is the right color
            if piece.color != player_turn:
                # raise exception indicating the player is interacting with the wrong color pieces
                raise InvalidMoveException('Wrong color piece.')     

            # Run move handler for the piece type
            match(type(piece)):
                case pawn.Pawn:
                    # Run pawn handler
                    piece_moved = self.__pawn_move_handler(self.board_spaces[start_space].occupying_piece, next_space, player_turn)
                    pass
                case _:
                    pass

        except:
            pass

        # Update piece has moved indicator. Only updates to True, never back to False
        if piece_moved:
            piece.has_moved = True

            # TODO: Check for king checks

        return piece_moved
    
    def __capture_piece(self, piece:piece.Piece):
        """
        Clears a space for a capture by removing the piece from the square and
        
        the pieces list, removing it from the game.
        Args:
            space_name: Name of space to clear ("A1", "A2", etc...)

        Returns:
            None          
        """
        # Pop the piece from the list to remove it from the game
        self.pieces.remove(piece)

        # Remove the sprite from the list so it no longer is drawn
        self.sprite_list.remove(piece.sprite)

        return

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
                cur_col = pawn.occupied_square.square_col
                cur_row = pawn.occupied_square.square_row
                next_col = next_space[0]
                next_row = int(next_space[1])
                if  cur_col == next_col :
                    # Pawn is staying in the same column. Check square(s) it is moving through.
                    for row in range(cur_row+direction, next_row+direction, direction):
                        if self.board_spaces[cur_col+str(row)].occupying_piece is not None:
                            # A piece occupies the row(s) ahead of the pawn. Raise an exception
                            raise InvalidMoveException('There is another piece blocking the way.')     

                else:
                    # Pawn is moving diagonally. Check destination for opposing color piece
                    # TODO: En passant
                    if self.board_spaces[next_space].occupying_piece is None \
                    or pawn.color == self.board_spaces[next_space].occupying_piece.color:
                        # There's no piece to capture. Raise an exception
                        raise InvalidMoveException('Pawns can only move diagonally when capturing.')     
                    else:
                        # "Capture" the enemy piece by removing it from the list of pieces
                        self.__capture_piece(self.board_spaces[next_space].occupying_piece)
                        


                # No pieces occupying the spaces ahead of the pawn. Move it to the new space
                pawn.update_space(self.board_spaces[next_space])
                pawn_moved = True

                # TODO: Pawn promotion

            else:
                # Pawn move invalid. Raise an exception
                InvalidMoveException("Pawns can't move that way.")

        except:
            pass
            
        return pawn_moved
    

class InvalidMoveException(Exception):
    """
    Custom exception handler for when a move fails to execute.
    """
    def __init__(self, msg:str):

        """
        Notifies the player why the move they tried to make has failed.

        Args:
            msg: Message to display indicating why move could not complete

        Returns:
            None
        """
        super().__init__()
        print(f'Move failed! {msg}')
    

