
# SHAYAAN HASNAIN AHMAD
# 20I-0647
# SECTION A
# AI - ASSIGNMENT 3

import copy

# THIS FUNCTION CREATED A BOARD OF 9*9 
# THIS CREATED A CHESS BOARD AND THE PEICES ARE LABELLED AS INITIALS 
# FOR EXAMPLE B FOR BISHOP ... 

def create_chess_board():
    
    # Create an empty chess_board
    chess_board = [[' ' for _ in range(8)] for _ in range(8)]
    
    # Place the white pieces on the chess_board
    chess_board[0][0] = 'R'
    chess_board[0][1] = 'N'
    chess_board[0][2] = 'B'
    chess_board[0][3] = 'Q'
    chess_board[0][4] = 'K'
    chess_board[0][5] = 'B'
    chess_board[0][6] = 'N'
    chess_board[0][7] = 'R'
    for col in range(8):
        chess_board[1][col] = 'P'
    
    # Place the black pieces on the chess_board
    chess_board[7][0] = 'r'
    chess_board[7][1] = 'n'
    chess_board[7][2] = 'b'
    chess_board[7][3] = 'q'
    chess_board[7][4] = 'k'
    chess_board[7][5] = 'b'
    chess_board[7][6] = 'n'
    chess_board[7][7] = 'r'
    for col in range(8):
        chess_board[6][col] = 'p'
    
    return chess_board


# THIS FUNCTION IS THERE TO CHECK VALIDITY OF A MOVE
# CHECK IF A MOVE IS POSSIBLE OR NOT
# ALSO CHECKS IF THAT PARTICULAR MOVE IS VALID FOR THAT PEICE AS A PEICE CAN ONLY MOVE TO CERTAIN FIXED POSITIONS

def move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player):
    
    # Check that the starting position is not empty
    if chess_board[starting_row][starting_col] == ' ':
        return False
    
    # Check that the destination position is not occupied by a friendly piece
    if chess_board[ending_row][ending_col].isupper() and player == 'black':
        return False
    if chess_board[ending_row][ending_col].islower() and player == 'white':
        return False
    
    # Check that the move is valid for the piece type
    piece = chess_board[starting_row][starting_col].lower()
    if piece == 'p':
        return pawn_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player)
    elif piece == 'r':
        return rook_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player)
    elif piece == 'n':
        return knight_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player)
    elif piece == 'b':
        return bishop_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player)
    elif piece == 'q':
        return queen_move_validity(chess_board, starting_row, starting_col, ending_row, ending_col, player)
    elif piece == 'k':
        return king_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player)
    
    # Invalid piece type
    return False

# ===========   VALIDITY CHECK FOR THE PEICES  ==============

# VALIDITY CHECK FOR PAWN

def pawn_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player):
   
    # Check that the pawn is moving forward
    if player == 'white':
        if starting_row >= ending_row:
            return False
    else:
        if starting_row <= ending_row:
            return False
    
    # Check that the pawn is moving in a straight line
    if starting_col != ending_col:
        # Check for diagonal capture
        if abs(starting_col - ending_col) != 1:
            return False
        if chess_board[ending_row][ending_col] == ' ':
            return False
    else:
        # Check for single or double move
        if abs(starting_row - ending_row) > 2:
            return False
        if abs(starting_row - ending_row) == 2 and (starting_row != 1 and starting_row != 6):
            return False
        if starting_row == ending_row:
            return False
        if chess_board[ending_row][ending_col] != ' ':
            return False
    
    return True

# VALIDITY CHECK FOR ROOK

def rook_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player):
    
    # check if rook is being moved to its current position
    if starting_row == ending_row and starting_col == ending_col:
        return False

    # check if the piece being moved is a rook
    if chess_board[starting_row][starting_col].lower() != 'r':
        return False

    # check if the destination position is out of board
    if ending_row < 0 or ending_row > 7 or ending_col < 0 or ending_col > 7:
        return False

    # check if the rook is moving along a straight line
    if starting_row != ending_row and starting_col != ending_col:
        return False

    # check if there are any pieces between source and destination
    if starting_row == ending_row:
        if starting_col > ending_col:
            col_range = range(ending_col+1, starting_col)
        else:
            col_range = range(starting_col+1, ending_col)
        for col in col_range:
            if chess_board[starting_row][col] != ' ':
                return False
    else:
        if starting_row > ending_row:
            row_range = range(ending_row+1, starting_row)
        else:
            row_range = range(starting_row+1, ending_row)
        for row in row_range:
            if chess_board[row][starting_col] != ' ':
                return False

    # check if the destination position is empty or occupied by opponent's piece
    if chess_board[ending_row][ending_col] == ' ' or chess_board[ending_row][ending_col].islower() != player.islower():
        return True
    else:
        return False


# BISHOP VALIDITY CHECK

def bishop_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player):
  
    # Check that the bishop is moving diagonally
    if abs(starting_row - ending_row) != abs(starting_col - ending_col):
        return False

   
    # Check for obstructions along the path
    row_dir = 1 if ending_row > starting_row else -1
    col_dir = 1 if ending_col > starting_col else -1
    row = starting_row + row_dir
    col = starting_col + col_dir
    while row != ending_row and col != ending_col:
        if chess_board[row][col] != ' ':
            return False
        row += row_dir
        col += col_dir

    return True


# VALIDITY CHECK FOR THE QUEEN 

def queen_move_validity(chess_board, starting_row, starting_col, ending_row, ending_col, player):
    
    # Check that the queen is moving in a straight line or diagonally
    if starting_row != ending_row and starting_col != ending_col:
        if abs(starting_row - ending_row) != abs(starting_col - ending_col):
            return False

 
    # Check for obstructions along the path
    if starting_row == ending_row:
        # Horizontal move
        for col in range(min(starting_col, ending_col) + 1, max(starting_col, ending_col)):
            if chess_board[starting_row][col] != ' ':
                return False
    elif starting_col == ending_col:
        # Vertical move
        for row in range(min(starting_row, ending_row) + 1, max(starting_row, ending_row)):
            if chess_board[row][starting_col] != ' ':
                return False
    else:
        # Diagonal move
        row_dir = 1 if ending_row > starting_row else -1
        col_dir = 1 if ending_col > starting_col else -1
        row = starting_row + row_dir
        col = starting_col + col_dir
        while row != ending_row and col != ending_col:
            if chess_board[row][col] != ' ':
                return False
            row += row_dir
            col += col_dir

    return True

#VALIDITY CHECK FOR THE KNIGHT 

def knight_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player):
    
    # Check if the destination cell is occupied by the player's own piece
    if chess_board[ending_row][ending_col].islower() == chess_board[starting_row][starting_col].islower():
        return False
    
    # Check if the move is L-shaped
    row_diff = abs(ending_row - starting_row)
    col_diff = abs(ending_col - starting_col)
    if not ((row_diff == 1 and col_diff == 2) or (row_diff == 2 and col_diff == 1)):
        return False
    
    return True


# VALIDITY CHECK FOR THE KING

def king_move_validity_check(chess_board, starting_row, starting_col, ending_row, ending_col, player):
   
    # Check that the king is moving to an adjacent cell
    if abs(starting_row - ending_row) > 1 or abs(starting_col - ending_col) > 1:
        return False


    return True


# =====================================================



# MOVE THE PEICE TAKES ARGUEMENT STARING ROW COL, ENDING ROW, COL
# CHECKS VALIDITY
# MAKES MOVE

def move_piece(chess_board, starting_row, starting_col, ending_row, ending_col):
    
    piece = chess_board[starting_row][starting_col]
    chess_board[starting_row][starting_col] = ' '
    chess_board[ending_row][ending_col] = piece
    display_board(chess_board) #display board after making move



   # FUNCTION THAT CHECKS FOR CHECKMATE  

   #To achieve checkmate, a player must put their opponent's king in a position where it cannot escape capture by any of the opponent's 
   #own pieces, either by direct capture or by blocking all possible escape squares.

def check_checkmate(chess_board, player):
   
    # Check if the player is in check
    if is_check(chess_board, player):
        # Check if the player has any valid moves
        for row in range(len(chess_board)):
            for col in range(len(chess_board[row])):
                if chess_board[row][col].lower() == player:
                    for dest_row in range(len(chess_board)):
                        for dest_col in range(len(chess_board[dest_row])):
                            if move_validity_check(chess_board, row, col, dest_row, dest_col):
                                # Simulate the move to see if it results in check
                                temp_chess_board = copy.deepcopy(chess_board)
                                move_piece(temp_chess_board, row, col, dest_row, dest_col)
                                if not is_check(temp_chess_board, player):
                                    return False
        return True
    else:
        return False

def is_check(chess_board, player):
    
    # Find the position of the player's king

    king_pos = None
    for row in range(len(chess_board)):
        for col in range(len(chess_board[row])):
            if chess_board[row][col].lower() == 'k' and chess_board[row][col].isupper() == (player == 'white'):
                king_pos = (row, col)
                break
        if king_pos is not None:
            break
    
    # Check if any of the opponent's pieces can capture the king

    for row in range(len(chess_board)):
        for col in range(len(chess_board[row])):
            piece = chess_board[row][col]
            if piece != ' ' and piece.isupper() != (player == 'white'):
                if move_validity_check(chess_board, row, col, king_pos[0], king_pos[1], player):
                    return True
    
    return False

# FUNCTION FOR CHECKING STALEMATE
# stalemate is a situation where a player whose king is not in check has no legal move to make.

def check_stalemate(chess_board, player):
   
    # Check if the player is not in check and has no valid moves

    if not is_check(chess_board, player):
        for row in range(len(chess_board)):
            for col in range(len(chess_board[row])):
                if chess_board[row][col].lower() == player:
                    for dest_row in range(len(chess_board)):
                         for dest_col in range(len(chess_board[dest_row])):
                            if move_validity_check(chess_board, row, col, dest_row, dest_col):
                                temp_chess_board = copy.deepcopy(chess_board)
                                move_piece(temp_chess_board, row, col, dest_row, dest_col)
                                if not is_check(temp_chess_board, player):
                                    return False
        return True
    else:
        return False


# evaluates the board and returns score 

def evaluate_board(chess_board, player):
    score = 0
    for row in range(len(chess_board)):
        for col in range(len(chess_board[row])):
            piece = chess_board[row][col]
            if piece == ' ':
                continue
            piece_score = piece_value[piece.lower()]
            if piece.isupper() == player.isupper():
                # Player's piece
                score += piece_score
            else:
                # Opponent's piece
                score -= piece_score
    return score

#  Returns a list of all possible moves for the given player on the given chess_board

def get_all_moves(chess_board, player):
    
    moves = []
    for row in range(len(chess_board)):
        for col in range(len(chess_board[row])):
            if chess_board[row][col].lower() == player:
                for dest_row in range(len(chess_board)):
                    for dest_col in range(len(chess_board[dest_row])):
                        if move_validity_check(chess_board, row, col, dest_row, dest_col):
                            moves.append(((row, col), (dest_row, dest_col)))
    return moves



piece_value = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 100}  #ALL THE SCORES ARE DEFINED HERE


# MINIMAX ALPHA BETA PRUNING USED HERE
# MINIMAX ALGORITH USED
# The function takes as input the current chess board, the current player,
# the search depth, the alpha and beta values, and a boolean indicating whether we are maximizing or minimizing the player. 
# The implementation uses recursion to explore the possible moves and evaluate them using the evaluate_board function. 

# If the search depth is zero or if the game is over (either checkmate or stalemate), the function returns the evaluation of the board.
#  Otherwise, it generates all possible moves for the current player and evaluates them using recursion.


def minimax_alpha_beta(chess_board, player, depth, alpha, beta, maximizing_player):
    if depth == 0 or check_checkmate(chess_board, player) or check_stalemate(chess_board, player):
        return evaluate_board(chess_board, player)

    moves = get_all_moves(chess_board, player)

    if maximizing_player:
        max_eval = float('-inf')
        for move in moves:
            temp_chess_board = copy.deepcopy(chess_board)
            move_piece(temp_chess_board, move[0], move[1], move[2], move[3])
            eval = minimax_alpha_beta(temp_chess_board, player, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in moves:
            temp_chess_board = copy.deepcopy(chess_board)
            move_piece(temp_chess_board, move[0], move[1], move[2], move[3])
            eval = minimax_alpha_beta(temp_chess_board, player, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


# display board

def display_board(chess_board):
    """
    Displays the chess chess_board with the pieces in their current positions
    """
    print('  ' + ' '.join([chr(i) for i in range(97, 105)]))
    print(' +' + '-' * 8 + '+')
    for row in range(8):
        print(str(row + 1) + '|' + ' '.join(chess_board[row]) + '|' + str(row + 1))
    print(' +' + '-' * 8 + '+')
    print('  ' + ' '.join([chr(i) for i in range(97, 105)]))


# Returns the best move for the computer player using the Min-Max algorithm with Alpha-Beta Pruning
# The function takes as input the current chess board and the player who is making the move.

#The function first defines the maximum depth for the search and initializes the best move and its score to None and negative infinity, respectively.

# It then generates all possible moves for the current player using the get_all_moves function and loops over each move.
# For each move, it makes a copy of the chess board and simulates the move using the move_piece function. 
# It then evaluates the move using the minimax_alpha_beta function with alpha set to negative infinity and beta set to positive infinity,
# and a maximum depth of six minus one (i.e., five).
def AI_moves(chess_board, player):
   
        # Define the maximum depth for the search
        max_depth = 6
        
        # Initialize the best move and its score
        best_move = None
        best_score = float('-inf')
    
        # Generate all possible moves for the current player
        moves = get_all_moves(chess_board, player)
        
        # Loop over the moves and evaluate each one using the Min-Max algorithm with Alpha-Beta Pruning
        for move in moves:
            # Make a copy of the chess_board and simulate the move
            temp_chess_board = copy.deepcopy(chess_board)
            move_piece(temp_chess_board, move[0], move[1], move[2], move[3])
            
            # Evaluate the move using the Min-Max algorithm with Alpha-Beta Pruning
            score = minimax_alpha_beta(temp_chess_board, player, float('-inf'), float('inf'), max_depth - 1)
            
            # Update the best move and its score if necessary
            if score > best_score:
                best_move = move
                best_score = score
            
        display_board(chess_board)   
        
        # Return the best move
        return best_move


def user_moves(chess_board, player):
    """
    Asks the user to enter their move and returns the starting and ending positions
    """
    while True:
        try:
            move = input("Please Enter your move (with starting and ending position) (e.g. 'e3 e5'): ")
            from_pos, to_pos = move.split()
            starting_row, starting_col = 8 - int(from_pos[1]), ord(from_pos[0]) - 97
            to_row, ending_col = 8 - int(to_pos[1]), ord(to_pos[0]) - 97
            
            if not move_validity_check(chess_board, starting_row, starting_col, to_row, ending_col, player):
                raise ValueError("Invalid move")
            
            display_board(chess_board)
            
            return starting_row, starting_col, to_row, ending_col
        
        except ValueError as e:
            print(e)


def get_opponent(player):
    """
    Returns the opponent of the given player
    """
    if player == 'W':
        return 'B'
    else:
        return 'W'
    
    

def play_game():
    chess_board = create_chess_board()
    display_board(chess_board)
    player = 'A'
    while True:
        print(f"Player {player}'s turn")
        if player == 'A':
            starting_row, starting_col, ending_row, ending_col = user_moves(chess_board, player)
        else:
            starting_row, starting_col, ending_row, ending_col = AI_moves(chess_board, player)
            print(f"Computer moves {chr(starting_col + 65)}{8 - starting_row} to {chr(ending_col + 65)}{8 - ending_row}")
        move_piece(chess_board, starting_row, starting_col, ending_row , ending_col)
        display_board(chess_board)
        if check_checkmate(chess_board, player):
            print(f"Player {player} is in checkmate! Player {get_opponent(player)} wins!")
            break
        elif check_stalemate(chess_board, player):
            print("Game is a draw!")
            break
        player = get_opponent(player)















play_game()