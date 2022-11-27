"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1
    
    if count_x > count_o:
        return O

    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    
    # Records all position that does not have X or O
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        return board
    
    # Uses deepcopy to avoid the original board from being modified
    new_board = copy.deepcopy(board)

    new_board[action[0]][action[1]] = player(board)
    
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Alignments that will make X win
    diag_x1 = board[0][0] == X and board[1][1] == X and board[2][2] == X
    diag_x2 = board[0][2] == X and board[1][1] == X and board[2][0] == X
    vert_x1 = board[0][0] == X and board[1][0] == X and board[2][0] == X
    vert_x2 = board[0][1] == X and board[1][1] == X and board[2][1] == X
    vert_x3 = board[0][2] == X and board[1][2] == X and board[2][2] == X
    horiz_x1 = board[0][0] == X and board[0][1] == X and board[0][2] == X
    horiz_x2 = board[1][0] == X and board[1][1] == X and board[1][2] == X
    horiz_x3 = board[2][0] == X and board[2][1] == X and board[2][2] == X

    # Alignments that will make O win
    diag_o1 = board[0][0] == O and board[1][1] == O and board[2][2] == O
    diag_o2 = board[0][2] == O and board[1][1] == O and board[2][0] == O
    vert_o1 = board[0][0] == O and board[1][0] == O and board[2][0] == O
    vert_o2 = board[0][1] == O and board[1][1] == O and board[2][1] == O
    vert_o3 = board[0][2] == O and board[1][2] == O and board[2][2] == O
    horiz_o1 = board[0][0] == O and board[0][1] == O and board[0][2] == O
    horiz_o2 = board[1][0] == O and board[1][1] == O and board[1][2] == O
    horiz_o3 = board[2][0] == O and board[2][1] == O and board[2][2] == O


    if diag_x1 or diag_x2 or vert_x1 or vert_x2 or vert_x3 or horiz_x1 or horiz_x2 or horiz_x3:
        return X
    elif diag_o1 or diag_o2 or vert_o1 or vert_o2 or vert_o3 or horiz_o1 or horiz_o2 or horiz_o3:
        return O


    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    # Checks if it's NOT a tie
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == None:
                return False
    
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    # If X turn we maximize value, if O turn we minimize value
    else:
        if player(board) == X:
            v, move = max_value(board)
            return move
        else:
            v, move = min_value(board)
    return move

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    move = None
    for action in actions(board):
        value, move1 = min_value(result(board, action))
        if value > v:
            v = value
            move = action    
            if v == 1:
                return v, move
    
    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    move = None
    for action in actions(board):
        value, move1 = max_value(result(board, action))
        if value < v:
            v = value
            move = action
            if v == -1:
                return v, move
    
    
    return v, move
