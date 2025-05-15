import math

def is_winner(board, player):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in line) for line in win_states)

def minimax(board, depth, is_max):
    if is_winner(board, 'O'): return 1
    if is_winner(board, 'X'): return -1
    if ' ' not in board: return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(board, depth+1, False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(board, depth+1, True))
                board[i] = ' '
        return best

def best_move(board):
    move = -1
    best_val = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False)
            board[i] = ' '
            if move_val > best_val:
                move = i
                best_val = move_val
    return move

board = [' ']*9
print("Best move index for O:", best_move(board))
