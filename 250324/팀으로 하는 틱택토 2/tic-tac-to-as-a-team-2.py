inp = [input() for _ in range(3)]

# Please write your code here.
tictactoe = [list(i) for i in inp]

column = [c for c in tictactoe]
row = [[tictactoe[j][i] for j in range(3)] for i in range(3)]
diagonal = [[tictactoe[0][0], tictactoe[1][1], tictactoe[2][2]], [tictactoe[2][0], tictactoe[1][1], tictactoe[0][2]]]

column_set = [set(c) for c in column]
row_set = [set(r) for r in row]
diagonal_set = [set(d) for d in diagonal]

count = 0
set_of_team = []
for c in column_set:
    if len(c) == 2:
        if c in set_of_team:
            continue
        set_of_team.append(c)
        count += 1
for r in row_set:
    if len(r) == 2:
        if r in set_of_team:
            continue
        set_of_team.append(r)
        count += 1
for d in diagonal_set:
    if len(d) == 2:
        if d in set_of_team:
            continue
        set_of_team.append(d)
        count += 1

print(count)