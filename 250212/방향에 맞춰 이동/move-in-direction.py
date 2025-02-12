n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Write your code here!
x, y = 0, 0

direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    if dir[i] == 'N':
        direction = 0
    elif dir[i] == 'E':
        direction = 1
    elif dir[i] == 'S':
        direction = 2
    elif dir[i] == 'W':
        direction = 3
    x = x + dx[direction] * dist[i]
    y = y + dy[direction] * dist[i]

print(f"{x} {y}")