n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
count, comfortable = 0, []

grid = [[0 for _ in range(n)] for _ in range(n)]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(m):
    y, x = points[i]
    x, y = x - 1, y - 1
    grid[y][x] = 1
    count = 0
    for j in range(4):
        if in_range(x + dx[j], y + dy[j]) and grid[y + dy[j]][x + dx[j]] == 1:
            count += 1
        
    if count == 3:
        comfortable.append(1)
    else:
        comfortable.append(0)

for comf in comfortable:
    print(comf)