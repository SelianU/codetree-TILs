N, M = map(int, input().split())

grid = [[0] * M for _ in range(N)]

def in_range(x, y):
    return 0 <= x and x < M and 0 <= y and y < N

x, y = 0, 0

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

direction = 2

number = 1

while number < N * M:
    grid[y][x] = number
    nx, ny = x + dx[direction], y + dy[direction]
    if in_range(nx, ny) and grid[ny][nx] == 0:
        x, y = x + dx[direction], y + dy[direction]
        number += 1
    else:
        direction = (direction - 1) % 4

grid[y][x] = number

for g in grid:
    for i in g:
        print(i, end=' ')
    print()