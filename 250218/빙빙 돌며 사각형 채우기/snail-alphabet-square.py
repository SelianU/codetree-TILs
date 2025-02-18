n, m = map(int, input().split())

# Write your code here!
a = ord('A')

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
dir = 1

grids = [[0] * m for _ in range(n)]

grids[y][x] = 'A'

def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n

while any(0 in row for row in grids):
    nx, ny = x + dx[dir], y + dy[dir]
    if in_range(nx, ny) and grids[ny][nx] == 0:
        if chr(a) == 'Z':
            a = ord('A')
        else:
            a += 1
        x, y = x + dx[dir], y + dy[dir]
        grids[y][x] = chr(a)
    else:
        dir = (dir + 1) % 4

for grid in grids:
    for g in grid:
        print(g, end=' ')
    print()
    