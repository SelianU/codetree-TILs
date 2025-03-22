n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# a와 b를 교환하고, c를 연다.

def change_cup(cup, move):
    cup[move[0]], cup[move[1]] = cup[move[1]], cup[move[0]]

def open_cup(cup, cup_open):
    if cup[cup_open] == 1:
        return True
    return False

answer = 0
for i in range(1, 4):
    cup = [0, 0, 0, 0]
    cup[i] = 1
    count = 0
    for move in moves:
        change_cup(cup, move[:2])
        if open_cup(cup, move[2]):
            count += 1
    answer = max(answer, count)

print(answer)