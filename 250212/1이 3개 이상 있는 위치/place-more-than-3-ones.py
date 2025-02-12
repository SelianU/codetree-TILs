n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

cnts = [[0 for _ in range(n)] for _ in range(n)]

for x in range(len(grid)):
    for y in range(len(grid[x])):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n) and grid[nx][ny] == 1:
                cnts[x][y] += 1

answer = 0

for cnt in cnts:
    for k in cnt:
        if k > 2:
            answer += 1

print(answer)