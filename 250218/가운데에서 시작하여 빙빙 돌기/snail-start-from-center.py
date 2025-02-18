N = int(input())

x = y = N - 1
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
dir = 3

grids = [[0] * N for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

number = N * N

grids[y][x] = number

while any(0 in row for row in grids):
    nx, ny = x + dx[dir], y + dy[dir]
    if in_range(nx, ny) and grids[ny][nx] == 0:
        number -= 1
        x, y = nx, ny
        grids[y][x] = number
    else:
        dir = (dir + 1) % 4
    
for g in grids:
    print(*g)