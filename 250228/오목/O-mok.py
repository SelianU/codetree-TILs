board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
b_win = w_win = False
ans_x = ans_y = 0

dx = [-2, -1, 0, 1, 2]
dy = [-2, -1, 0, 1, 2]

for y_spot in range(2, 17):
    for x_spot in range(2, 17):
        if board[y_spot][x_spot] == 1:
            for i in range(5):
                if board[y_spot + dy[i]][x_spot + dx[i]] != 1:
                    break
                if i == 4:
                    b_win = True
            for i in range(5):
                if board[y_spot + dy[i]][x_spot - dx[i]] != 1:
                    break
                if i == 4:
                    b_win = True
            for i in range(5):
                if board[y_spot][x_spot + dx[i]] != 1:
                    break
                if i == 4:
                    b_win = True
            for i in range(5):
                if board[y_spot + dy[i]][x_spot] != 1:
                    break
                if i == 4:
                    b_win = True
        elif board[y_spot][x_spot] == 2:
            for i in range(5):
                if board[y_spot + dy[i]][x_spot + dx[i]] != 2:
                    break
                if i == 4:
                    w_win = True
            for i in range(5):
                if board[y_spot + dy[i]][x_spot - dx[i]] != 2:
                    break
                if i == 4:
                    w_win = True
            for i in range(5):
                if board[y_spot][x_spot + dx[i]] != 2:
                    break
                if i == 4:
                    w_win = True
            for i in range(5):
                if board[y_spot + dy[i]][x_spot] != 2:
                    break
                if i == 4:
                    w_win = True
        if b_win or w_win:
            ans_x, ans_y = x_spot + 1, y_spot + 1
            break
    if b_win or w_win:
        break

if b_win:
    print(1)
    print(ans_y, ans_x)
elif w_win:
    print(2)
    print(ans_y, ans_x)
else:
    print(0)