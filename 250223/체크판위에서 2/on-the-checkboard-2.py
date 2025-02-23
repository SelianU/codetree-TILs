R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Write your code here!
count = 0

for i in range(1, R - 1):
    for j in range(1, C - 1):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                if grid[0][0] == 'W' and grid[i][j] == 'B' and grid[k][l] == 'W':
                    count += 1
                elif grid[0][0] == 'B' and grid[i][j] == 'W' and grid[k][l] == 'B':
                    count += 1

print(count)