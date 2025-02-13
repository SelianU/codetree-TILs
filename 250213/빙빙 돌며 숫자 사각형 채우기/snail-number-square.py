n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Write your code here!
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n

x, y = 0, 0

arr[y][x] = 1

dir = 1

for i in range(2, m * n + 1):
    nx, ny = x + dx[dir], y + dy[dir]

    if not in_range(nx, ny) or arr[ny][nx] != 0:
        dir = (dir + 1) % 4
    
    x, y = x + dx[dir], y + dy[dir]
    arr[y][x] = i

for ar in arr:
    for a in ar:
        print(a, end=' ')
    print()