def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == row - i:
            return False
    return True
def solve(row, board):
    if row == 8:
        return board
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            result = solve(row + 1, board)
            if result:
                return result
    return None
solution = solve(0, [0]*8)
for r in range(8):
    line = ['Q' if solution[r] == c else '.' for c in range(8)]
    print(' '.join(line))
