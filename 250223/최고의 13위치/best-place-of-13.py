n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
max_num = 0

for i in range(n):
    for j in range(n - 2):
        max_num = max(grid[i][j] + grid[i][j + 1] + grid[i][j + 2], max_num)

print(max_num)