n = int(input())
li = [[0 for _ in range(n)] for _ in range(n)]

num = 1

for i in range(n):
    for j in range(n):
        li[j if i % 2 != 0 else n - j - 1][n - i - 1] = num
        num += 1

for i in range(n):
    for j in range(n):
        print(li[i][j], end=' ')
    print()