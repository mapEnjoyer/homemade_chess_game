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
        - pieces: List of all pieces in the game
        - sprite_list: List of sprites to be drawn on screen
        - king_checks: List of active king checks
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
        text_file_path = str(Path(__file__).parent / "textures" / constants.white_pawn_image_name)
        
        self.pieces.append(pawn.Pawn(self.board_spaces["A2"], text_file_path, constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["B2"], text_file_path, constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["C2"], text_file_path, constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["D2"], text_file_path, constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["E2"], text_file_path, constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["F2"], text_file_path, constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["G2"], text_file_path, constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["H2"], text_file_path, constants.pawn_image_width))

        # Create A1/H1 rooks
        text_file_path = str(Path(__file__).parent / "textures" / constants.white_rook_image_name)

        self.pieces.append(rook.Rook(self.board_spaces["A1"], text_file_path, constants.rook_image_width))
        self.pieces.append(rook.Rook(self.board_spaces["H1"], text_file_path, constants.rook_image_width))

        # Create B1/G1 knights
        text_file_path = str(Path(__file__).parent / "textures" / constants.white_knight_image_name)

        self.pieces.append(knight.Knight(self.board_spaces["B1"], text_file_path, constants.knight_image_width))
        self.pieces.append(knight.Knight(self.board_spaces["G1"], text_file_path, constants.knight_image_width))

        # Create C1/F1 bishops
        text_file_path = str(Path(__file__).parent / "textures" / constants.white_bishop_image_name)

        self.pieces.append(bishop.Bishop(self.board_spaces["C1"], text_file_path, constants.bishop_image_width))
        self.pieces.append(bishop.Bishop(self.board_spaces["F1"], text_file_path, constants.bishop_image_width))

        # Create D1 queen
        text_file_path = str(Path(__file__).parent / "textures" / constants.white_queen_image_name)

        self.pieces.append(queen.Queen(self.board_spaces["D1"], text_file_path, constants.queen_image_width))

        # Create E1 king
        text_file_path = str(Path(__file__).parent / "textures" / constants.white_king_image_name)

        self.pieces.append(king.King(self.board_spaces["E1"], text_file_path, constants.king_image_width))

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
        text_file_path = str(Path(__file__).parent / "textures" / constants.black_pawn_image_name)

        self.pieces.append(pawn.Pawn(self.board_spaces["A7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["B7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["C7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["D7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["E7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["F7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["G7"], text_file_path.__str__(), constants.pawn_image_width))
        self.pieces.append(pawn.Pawn(self.board_spaces["H7"], text_file_path.__str__(), constants.pawn_image_width))

        # Create A8/H8 rooks
        text_file_path = str(Path(__file__).parent / "textures" / constants.black_rook_image_name)

        self.pieces.append(rook.Rook(self.board_spaces["A8"], text_file_path.__str__(), constants.rook_image_width))
        self.pieces.append(rook.Rook(self.board_spaces["H8"], text_file_path.__str__(), constants.rook_image_width))

        # Create B8/G8 knights
        text_file_path = str(Path(__file__).parent / "textures" / constants.black_knight_image_name)

        self.pieces.append(knight.Knight(self.board_spaces["B8"], text_file_path.__str__(), constants.knight_image_width))
        self.pieces.append(knight.Knight(self.board_spaces["G8"], text_file_path.__str__(), constants.knight_image_width))

        # Create C8/F8 bishops
        text_file_path = str(Path(__file__).parent / "textures" / constants.black_bishop_image_name)

        self.pieces.append(bishop.Bishop(self.board_spaces["C8"], text_file_path.__str__(), constants.bishop_image_width))
        self.pieces.append(bishop.Bishop(self.board_spaces["F8"], text_file_path.__str__(), constants.bishop_image_width))   

        # Create D8 queen
        text_file_path = str(Path(__file__).parent / "textures" / constants.black_queen_image_name)

        self.pieces.append(queen.Queen(self.board_spaces["D8"], text_file_path.__str__(), constants.queen_image_width))

        # Create E8 king
        text_file_path = str(Path(__file__).parent / "textures" / constants.black_king_image_name)
        
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
            
            if piece is None:
                # No piece to move on that square. Raise an exception
                raise InvalidMoveException('No piece to move.')
            
            if not isinstance(piece, piece_type):
                # Piece on the square does not match the command. Raise an exception
                raise InvalidMoveException('Wrong piece type.')

            # Check that the piece being moved is the right color
            if piece.color != player_turn:
                # raise exception indicating the player is interacting with the wrong color pieces
                raise InvalidMoveException('Wrong color piece.')

            # Run move handler for the piece type
            match(type(piece)):
                case pawn.Pawn:
                    # Run pawn handler
                    piece_moved = self.__pawn_move_handler(self.board_spaces[start_space].occupying_piece, next_space)
                    pass
                case knight.Knight:
                    # Run knight handler
                    piece_moved = self.__knight_move_handler(self.board_spaces[start_space].occupying_piece, next_space)
                    pass
                case bishop.Bishop:
                    # Run bishop handler
                    piece_moved = self.__bishop_move_handler(self.board_spaces[start_space].occupying_piece, next_space)
                    pass
                case rook.Rook:
                    # Run rook handler
                    piece_moved = self.__rook_move_handler(self.board_spaces[start_space].occupying_piece, next_space)
                    pass
                case queen.Queen:
                    # Run queen handler
                    piece_moved = self.__queen_move_handler(self.board_spaces[start_space].occupying_piece, next_space)
                    pass
                case king.King:
                    # Run king handler
                    piece_moved = self.__king_move_handler(self.board_spaces[start_space].occupying_piece, next_space)
                case _:
                    pass

        except:
            pass

        if piece_moved:
            # Check for game over
            for piece in self.pieces:
                if isinstance(piece, king.King) and piece.color != player_turn:
                    if self.__game_over(piece):
                        # TODO: Game is over!
                        pass

        return piece_moved

    def __move_piece(self, piece_to_move:piece.Piece, next_space:str):
        """
        Moves a piece by performing the following steps:
            - Resolving captures if necessary
            - Updating piece's occupied space
        Args:
            piece: piece to move
            next_space: space to move to. Space must match one of the spaces found in constants.space_names

        Returns:
            piece_moved: boolean True if piece moved, False otherwise     
        """
        piece_moved = False
        piece_to_cap = self.board_spaces[next_space].occupying_piece
        original_space = piece_to_move.occupied_square

        try:
            if piece_to_cap is None or piece_to_move.color != piece_to_cap.color:
                if piece_to_cap is not None:
                    # Remove the piece from the game
                    self.pieces.remove(piece_to_cap)

                    # Remove the sprite from the list so it no longer is drawn
                    self.sprite_list.remove(piece_to_cap.sprite)

                # Move the piece to the new space
                piece_to_move.update_space(self.board_spaces[next_space])

                # Now that the piece has moved, run a check on the king of the same color.
                # If the move would put the king into check, we have to reverse it and
                # deny the move.
                for piece in self.pieces:
                    if isinstance(piece, king.King) and piece.color == piece_to_move.color:
                        if self.__determine_checks(piece.occupied_square.name):
                            # This move would put the king in check. Undo it by 
                            # reverting the board state and throwing an exception
                            piece_to_move.update_space(original_space)

                            if piece_to_cap is not None:
                                # Add the piece back to the list of pieces
                                self.pieces.append(piece_to_cap)

                                # Add the piece's sprite back to the sprite list
                                self.sprite_list.append(piece_to_cap.sprite)

                                # Update the piece's square to the space it already thinks it's on.
                                # This is to ensure the references between space and piece match.
                                piece_to_cap.update_space(piece_to_cap.occupied_square)
                            
                            raise InvalidMoveException(f'This move would put your king in check!')
                        else:
                            break

                # Indicate that piece has moved
                piece_moved = True
                piece_to_move.has_moved = True

            else:
                # Space is occupied by a piece of the same color. Throw an exception.
                raise InvalidMoveException("There is another piece blocking the way.")

        except:
            pass
        
        return piece_moved

    def __pawn_move_handler(self, pawn:pawn.Pawn, next_space:str):
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
        cur_col_idx = constants.board_col_labels.index(pawn.occupied_square.square_col)
        nxt_col_idx = constants.board_col_labels.index(next_space[0])

        try:
            if pawn.is_move_valid(next_space) == True:

                if  cur_col_idx == nxt_col_idx :
                    # Pawn is staying in the same column. Run standard collision check
                    self.__check_collisions(pawn.occupied_square.name, next_space)

                    # Assuming no exception was raised, the move is valid. Attempt to move the pawn
                    pawn_moved = self.__move_piece(pawn, next_space)                       

                else:
                    # Pawn is moving diagonally. Check destination for opposing color piece
                    # TODO: En passant
                    if self.board_spaces[next_space].occupying_piece is None \
                    or pawn.color == self.board_spaces[next_space].occupying_piece.color:
                        # There's no piece to capture. Raise an exception
                        raise InvalidMoveException('Pawns can only move diagonally when capturing.')     
                    else:
                        # There is a piece to capture. Attempt to move the pawn
                        pawn_moved = self.__move_piece(pawn, next_space)

                # TODO: Pawn promotion

            else:
                # Pawn move invalid. Raise an exception
                InvalidMoveException("Pawns can't move that way.")

        except:
            pass
            
        return pawn_moved
    
    def __knight_move_handler(self, knight:knight.Knight, next_space:str):
        """
        Handles knight moves by first checking if the move between the spaces is
        technically viable per how the knight moves. If so, the destination space
        is checked for captures. No collision detection needed as knights are the
        only piece that can pass thorugh others.

        Args:
            knight: Knight object being moved.
            next_space: space to move to. Space must match one of the spaces found in constants.space_names

        Returns:
            knight_moved: Boolean True if knight moved, False otherwise  
        """
        knight_moved = False

        try:
            if knight.is_move_valid(next_space) == True:
                # Check for piece at the destination. If it is the opposite color, we can capture
                knight_moved = self.__move_piece(knight, next_space)

            else:
                # Knight move invalid. Raise an exception
                raise InvalidMoveException("Knights can't move that way.")

        except:
            pass

        return knight_moved

    def __bishop_move_handler(self, bishop:bishop.Bishop, next_space:str):
        """
        Handles bishop moves by first checking if the move between the spaces is
        technically viable per how the bishop moves. If so, the destination space
        and spaces in between are checked for captures. 

        Args:
            bishop: Bishop object being moved.
            next_space: space to move to. Space must match one of the spaces found in constants.space_names

        Returns:
            bishop_moved: Boolean True if bishop moved, False otherwise  
        """
        bishop_moved = False

        try:
            if bishop.is_move_valid(next_space) == True:

                # Check for collisions
                self.__check_collisions(bishop.occupied_square.name, next_space)     

                # No pieces in the way. We can attempt to move
                bishop_moved = self.__move_piece(bishop, next_space)

            else:
                # Bishop move invalid. Raise an exception
                raise InvalidMoveException("Bishops can't move that way.")
                
        except:
            pass

        return bishop_moved

    def __rook_move_handler(self, rook:rook.Rook, next_space:str):
        """
        Handles rook moves by first checking if the move between the spaces is
        technically viable per how the rook moves. If so, the destination space
        and spaces in between are checked for captures. 

        Args:
            rook: Rook object being moved.
            next_space: space to move to. Space must match one of the spaces found in constants.space_names

        Returns:
            rook_moved: Boolean True if rook moved, False otherwise  
        """
        rook_moved = False

        try:
            if rook.is_move_valid(next_space) == True:

                # Check for collisions
                self.__check_collisions(rook.occupied_square.name, next_space)     

                # No pieces in the way. We can attempt to move
                rook_moved = self.__move_piece(rook, next_space)

            else:
                # Rook move invalid. Raise an exception
                raise InvalidMoveException("Rooks can't move that way.")
                
        except:
            pass

        return rook_moved

    def __queen_move_handler(self, queen:queen.Queen, next_space:str):
        """
        Handles queen moves by first checking if the move between the spaces is
        technically viable per how the queen moves. If so, the destination space
        and spaces in between are checked for captures. 

        Args:
            queen: Queen object being moved.
            next_space: space to move to. Space must match one of the spaces found in constants.space_names

        Returns:
            queen_moved: Boolean True if queen moved, False otherwise  
        """
        queen_moved = False

        try:
            if queen.is_move_valid(next_space) == True:

                # Check for collisions
                self.__check_collisions(queen.occupied_square.name, next_space)        

                # No pieces in the way. We can attempt to move
                queen_moved = self.__move_piece(queen, next_space)

            else:
                # Queen move invalid. Raise an exception
                raise InvalidMoveException("Queens can't move that way.")
                
        except:
            pass

        return queen_moved

    def __king_move_handler(self, king:king.King, next_space:str):
        """
        Handles king moves by first checking if the move between the spaces is
        technically viable per how the king moves. If so, the destination space
        and spaces in between are checked for captures. 

        Args:
            king: King object being moved.
            next_space: space to move to. Space must match one of the spaces found in constants.space_names

        Returns:
            king_moved: Boolean True if king moved, False otherwise  
        """
        king_moved = False

        try:
            if king.is_move_valid(next_space) == True:

                if king.is_castleing(next_space):
                    # Raise an exception if the king has already moved this game
                    if king.has_moved:
                        raise InvalidMoveException(f'The king has already moved! It can no longer castle!')

                    # King is attempting castle, check for collisions along the way
                    self.__check_collisions(king.occupied_square.name, next_space)
                    if self.board_spaces[next_space].occupying_piece is not None:
                        raise InvalidMoveException(f'There is another piece blocking the way.')

                    # TODO: No collisions, look for checks on the squares the king is passing through and the destination

                    # Determine rook square info based on which king is castleing in which direction
                    match (king.color, next_space):
                        case (constants.PlayerColor.WHITE, 'C1'):
                            rook_start_square = 'A1'
                            rook_end_squre = 'D1'

                        case (constants.PlayerColor.WHITE, 'G1'):
                            rook_start_square = 'H1'
                            rook_end_squre = 'F1'

                        case (constants.PlayerColor.BLACK, 'C8'):
                            rook_start_square = 'A8'
                            rook_end_squre = 'D8'                            

                        case (constants.PlayerColor.BLACK, 'G8'):
                            rook_start_square = 'H8'
                            rook_end_squre = 'F8'

                        case _:
                            raise InvalidMoveException(f'How did this even happen?')

                    # Make sure there the rook on the starting square is still there and hasn't moved
                    if self.board_spaces[rook_start_square].occupying_piece is None or self.board_spaces[rook_start_square].occupying_piece.has_moved:
                        raise InvalidMoveException(f'Cannot castle, the rook on {rook_start_square} has moved!')

                    # Move the king and rook to complete the castle
                    king_moved = self.__move_piece(king, next_space)
                    self.__move_piece(self.board_spaces[rook_start_square].occupying_piece, rook_end_squre)  

                else:
                    king_moved = self.__move_piece(king, next_space)

            else:
                # King move invalid. Raise an exception
                raise InvalidMoveException("Kings can't move that way.")
                
        except:
            pass

        return king_moved
    
    def __check_collisions(self, cur_space:str, nxt_space:str):
        """
        Checks for collisions for rook/bishops/queens moving along rows, columns or diagonals.
        Also used for pawns moving forward. An excpetion will be raised if a piece is in the way.

        Args:
            cur_space: string name of starting space ('A1', 'A2'...)
            nxt_space: string name of ending space ('A1', 'A2'...)

        Returns:
            Exception if piece is in the way
        """

        cur_col_idx = constants.board_col_labels.index(cur_space[0])
        cur_row_idx = constants.board_row_labels.index(cur_space[1])
        nxt_col_idx = constants.board_col_labels.index(nxt_space[0])
        nxt_row_idx = constants.board_row_labels.index(nxt_space[1])

        # Direction variables init to 0, will be set according to if the queen moves verically, horizontally or diagonally
        col_dir = 0
        row_dir = 0

        if cur_col_idx < nxt_col_idx:
            # Piece is moving towards H column
            col_dir = 1

        if cur_col_idx > nxt_col_idx:
            # Piece is moving towards A column
            col_dir = -1

        if cur_row_idx < nxt_row_idx:
            # Piece is moving towards row 8
            row_dir = 1

        if cur_row_idx > nxt_row_idx:
            # Piece is moving towards row 1
            row_dir = -1

        if col_dir and not row_dir:
            # Check along row up to but not including target square
            for col in range(cur_col_idx + col_dir, nxt_col_idx, col_dir):
                if self.board_spaces[constants.board_col_labels[col] + constants.board_row_labels[cur_row_idx]].occupying_piece is not None:
                    raise InvalidMoveException("There is another piece blocking the way.")

        elif row_dir and not col_dir:
            # Check along column up to but not including target square
            for row in range(cur_row_idx + row_dir, nxt_row_idx, row_dir):
                if self.board_spaces[constants.board_col_labels[cur_col_idx] + constants.board_row_labels[row]].occupying_piece is not None:
                    raise InvalidMoveException("There is another piece blocking the way.")

        else:
            # Check along diagonal up to but not including target square
            for col, row in zip(range(cur_col_idx + col_dir, nxt_col_idx, col_dir), range(cur_row_idx + row_dir, nxt_row_idx, row_dir)):
                if self.board_spaces[constants.board_col_labels[col] + constants.board_row_labels[row]].occupying_piece is not None:                    
                    raise InvalidMoveException("There is another piece blocking the way.")   

    def __determine_checks(self, king_space:str):
        """
        Method to look for checks for a king of a specific color on a given square.
        This method is intended to be a used for both king moves going to new squares
        and for pieces moving to other squares that could lead to a check.

        Args:
            king_space: string name of the space to look for checks ('A1', 'A2'...)

        Returns:
            king_checks: list of active checks
        """

        # Overarching plan is to check rows, columns and diagonals from the square in question. 
        # If we hit a piece of the same color, we have a blocker and don't need to keep checking. 
        # If we hit a piece of the opposing color, we need to check if it has a valid move to the 
        # king's square. If it does, the king is in check.

        try:
            # Clear list of king checks
            king_checks = []

            for col_dir in range (-1, 2):
                for row_dir in range(-1, 2):
                    # Check for king check going along indicated row/col/diagonal
                    king_check = self.__directional_king_checks(king_space, col_dir, row_dir)
                    if king_check:
                        # Add it to the list
                        king_checks.append(king_check)

            # Easier to brute for check specifically the enemy knights 
            # for checks rather than check around the king's square
            for piece in self.pieces:
                if isinstance(piece, knight.Knight) and piece.color != self.board_spaces[king_space].occupying_piece.color:
                    if piece.is_move_valid(king_space):
                        # Enemy knight has eyes on the king. He is in check
                        king_checks.append(KingCheck(self.board_spaces[king_space].occupying_piece, piece))

            if len(king_checks):
                # King is in check, raise exception for message to player
                raise KingInCheckException(self.board_spaces[king_space].occupying_piece.color)

        except:
            pass
        
        return king_checks
            
    def __directional_king_checks(self, king_space:str, col_dir:int, row_dir:int):
        """
        Helper method to __determine_checks() that checks directionally from the kings
        square looking for checks. If there is a check found, an exception will
        be raised.

        Args:
            king_space: string name of the space to look for checks ('A1', 'A2'...)
            col_dir: column direction. -1 to check towards A, +1 to check towards H, and 0 to stay in the current column
            row_dir: row direction. -1 to check towards 1, +1 to check towards 8, and 0 to stay in the current row

        Returns:
            king_check: KingCheck object created if king is in check 
        """
        cur_col_idx = constants.board_col_labels.index(king_space[0])
        cur_row_idx = constants.board_row_labels.index(king_space[1])
        king_check  = None

        # Determine starting and ending column
        match col_dir:
            case -1:
                col_end = -1

            case 1: 
                col_end = len(constants.board_col_labels)

            case _:
                pass

        # Determine starting and ending row
        match row_dir:
            case -1:
                row_end = -1

            case 1: 
                row_end = len(constants.board_row_labels)

            case _:
                pass

        if col_dir and not row_dir:
            # Check along row up to edge of board or first piece we hit, whichever is first
            for col in range(cur_col_idx + col_dir, col_end, col_dir):
                next_space = constants.board_col_labels[col] + constants.board_row_labels[cur_row_idx]
                if self.board_spaces[next_space].occupying_piece is not None:
                    # There is a piece on this space. Look for check, exception will be raised if there is one
                    king_check = self.__space_to_space_king_check(king_space, next_space)
                    break

        elif row_dir and not col_dir:
            # Check along columm up to edge of board or first piece we hit, whichever is first
            for row in range(cur_row_idx + row_dir, row_end, row_dir):
                next_space = constants.board_col_labels[cur_col_idx] + constants.board_row_labels[row]
                if self.board_spaces[next_space].occupying_piece is not None:
                    # There is a piece on this space. Look for check, exception will be raised if there is one
                    king_check = self.__space_to_space_king_check(king_space, next_space)
                    break

        elif row_dir and col_dir:
            # Check along diagonal up to edge of board or first piece we hit, whichever is first
            for col, row in zip(range(cur_col_idx + col_dir, col_end, col_dir), range(cur_row_idx + row_dir, row_end, row_dir)):
                next_space = constants.board_col_labels[col] + constants.board_row_labels[row]
                if self.board_spaces[next_space].occupying_piece is not None:
                    # There is a piece on this space. Look for check, exception will be raised if there is one
                    king_check = self.__space_to_space_king_check(king_space, next_space)
                    break

        return king_check

    def __space_to_space_king_check(self, king_space:str, piece_space:str):
        """
        Helper method to __directional_king_checks() that checks from king space
        to a piece's space if the king is in check. If there is a check found, an 
        exception will be raised.

        Args:
            king_space: string name of the king space ('A1', 'A2'...)
            piece_space: string name of the piece potentially checking the king('A1', 'A2'...)

        Returns:
            Raises excpetion if king is in check        
        """
        if self.board_spaces[piece_space].occupying_piece.color != self.board_spaces[king_space].occupying_piece.color and \
           self.board_spaces[piece_space].occupying_piece.is_move_valid(king_space):
            # Create a king check and return it
            return KingCheck(self.board_spaces[king_space].occupying_piece, self.board_spaces[piece_space].occupying_piece)

    def __game_over(self, king:king.King):
        """
        Method to check for game over on the king who is actively in check. The game is considered over if the following
        conditions are met:

        1. The king has no valid moves to get out of check.
        2. No piece of the same color can capture the checking piece(s).
        3. No piece can block the check.

        Args:
            king: King object to check game over for

        Returns:
            game_is_over: boolean True if game is over, false otherwise
        """
        game_is_over = False
        king_space_name = king.occupied_square.name

        # Look for checks on the king
        active_checks = self.__determine_checks(king_space_name)

        if active_checks:

            # Momentarily take the king off the board so that it can't be seen
            # as its own blocker in future check determinations
            king.occupied_square.occupying_piece = None
            king.occupied_square = None

            # King is in check. First look for a move to get out of the way
            for space in self.board_spaces[king_space_name].surrounding_spaces:
                if self.board_spaces[space].occupying_piece is None or self.board_spaces[space].occupying_piece.color != king.color:
                    # King can move to this square. Look for checks on the new square
                    if self.__determine_checks(space) is None:
                        # King has a valid move to get out of check. Game is not over
                        break

            # Put the king back on the board
            king.update_space(self.board_spaces[king_space_name])



        return game_is_over


class KingCheck():
    """
    King check class. Contains the king object in check and the piece causing the check.

    Attributes:
        - king_piece: King object in check
        - checking_piece: The piece causing the check
    """
    def __init__(self, king_piece:king.King, checking_piece:piece.Piece):
        """
        Initializes the king check object by storing the king in check and checking
        piece objects as attributes.
        
        Args:
            king_piece: King piece object
            checking_piece: Checking piece object
        Returns:
            None    
        """
        self.king_piece = king_piece
        self.checking_piece = checking_piece

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
    
class KingInCheckException(Exception):
    """
    Custom exception handler for when a king is in check
    """
    def __init__(self, king_color:constants.PlayerColor):

        """
        Notifies the player their king is in check

        Args:
            king_color: Color of the king in check. Modifies the displayed message.

        Returns:
            None
        """
        super().__init__()

        match king_color:
            case constants.PlayerColor.WHITE:
                print(f'The white king is in check!')

            case constants.PlayerColor.BLACK:
                print(f'The black king is in check!')

            case _:
                print(f'What color is the king? How is he in check?')
