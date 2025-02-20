N, T = map(int, input().split())

direction = input()

grid = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
dir = 0
x = y = (N - 1) // 2

answer = grid[y][x]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for i in range(T):
    if direction[i] == 'L':
        dir = (dir - 1) % 4
    elif direction[i] == 'R':
        dir = (dir + 1) % 4
    else:
        nx, ny = x + dx[dir], y + dy[dir]
        if in_range(nx, ny):
            x, y = x + dx[dir], y + dy[dir]
            answer += grid[y][x]

print(answer)