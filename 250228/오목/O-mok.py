board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
b_win = w_win = False
b_x = b_y = w_x = w_y = 0

def check_row(board, color):
    win = False
    x = y = 0
    for j in range(len(board)):
        count = 0
        for i in range(len(board[j]) - 5):
            if board[j][i] == color:
                count += 1
            else:
                count = 0
            if count == 5:
                x = i - 2
                y = j + 2
                win = True
                break
        if win:
            break
    return win, x, y

def check_column(board, color):
    win = False
    x = y = 0
    for i in range(len(board)):
        count = 0
        for j in range(len(board) - 5):
            if board[i][j] == color:
                count += 1
            else:
                count = 0
            if count == 5:
                x = i + 2
                y = j - 2
                win=True
                break
        if win:
            break
    return win, x, y

def check_diagonal(board, color):
    pass

b_row = check_row(board, 1)
b_col = check_column(board, 1)

w_row = check_row(board, 2)
w_col = check_column(board, 2)

if b_row[0]:
    print(1)
    print(b_row[1], b_row[2])
elif b_col[0]:
    print(1)
    print(b_col[1], b_col[2])
elif w_row[0]:
    print(2)
    print(w_row[1], w_row[2])
elif w_col[0]:
    print(2)
    print(w_col[1], w_col[2])
else:
    print(0)