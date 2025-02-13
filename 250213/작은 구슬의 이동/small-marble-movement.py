n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Write your code here!
matrix = [[0 for _ in range(n)] for _ in range(n)]

direction = {'U': 0, 'R': 1, 'D': 2, 'L': 3}

dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]

position = [r - 1, c - 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dir_num = direction[d]

for i in range(t):
    nx, ny = position[0] + dx[dir_num], position[1] + dy[dir_num]
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
        continue
    
    position = [position[0] + dx[dir_num], position[1] + dy[dir_num]]

for pos in position:
    print(pos + 1, end=' ')