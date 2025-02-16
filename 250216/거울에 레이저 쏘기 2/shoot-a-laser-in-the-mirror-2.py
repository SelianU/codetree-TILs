n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Write your code here!
# 어디서 어디로
def is_reflect(direction, mirror):
    reflect = 0
    if mirror == '/':
        reflect = 3 - direction
    elif mirror == '\\':
        if direction < 2:
            reflect = 1 - direction
        else:
            reflect = 5 - direction
    return reflect

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

direction = (k - 1) // n

# 초기 위치 설정
if direction == 0:
    x = k - 1
    y = 0
elif direction == 1:
    x = n - 1
    y = k - n - 1
elif direction == 2:
    x = 0 if k % n == 0 else n - k % n
    y = n - 1
else:
    x = 0
    y = 0 if k % n == 0 else n - k % n

count = 0

while True:
    direction = is_reflect(direction, grid[y][x])
    count += 1
    nx, ny = x + dx[direction], y + dy[direction]
    if in_range(nx, ny):
        x, y = x + dx[direction], y + dy[direction]
        if direction % 2 == 0:
            direction = 2 - direction
        else:
            direction = 4 - direction
    else:
        break

print(count)