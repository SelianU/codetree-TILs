n = int(input())

li = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        li[i][j] = li[i-1][j] + li[i-1][j-1] + li[i][j-1] if i > 0 and j > 0 else 1

for i in range(n):
    for j in range(n):
        print(li[i][j], end=' ')
    print()