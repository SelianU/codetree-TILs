N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
dir = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

x = y = 0
count = 0

for i in range(N):
    for j in range(M):
        for x_dir, y_dir in dir:
            if in_range(i + x_dir * 2, j + y_dir * 2) and arr[i][j] == 'L' and arr[i + x_dir][j + y_dir] == 'E' and arr[i + x_dir * 2][j + y_dir * 2] == 'E':
                count += 1

print(count)