def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, mark):
    for row in board:
        if all(s == mark for s in row): return True
    for col in zip(*board):
        if all(s == mark for s in col): return True
    if all(board[i][i] == mark for i in range(3)): return True
    if all(board[i][2 - i] == mark for i in range(3)): return True
    return False

board = [[" "]*3 for _ in range(3)]
turn = "X"

for _ in range(9):
    print_board(board)
    row = int(input(f"Player {turn}, enter row (0-2): "))
    col = int(input(f"Player {turn}, enter col (0-2): "))
    if board[row][col] == " ":
        board[row][col] = turn
        if check_winner(board, turn):
            print_board(board)
            print(f"Player {turn} wins!")
            break
        turn = "O" if turn == "X" else "X"
    else:
        print("Cell occupied!")
else:
    print("It's a draw!")
