n = int(input())
li = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n + 1):
    for j in range(n):
        li[i - 1][j] = i + n * j

for i in range(n):
    for j in range(n):
        print(li[i][j],end=" ")
    print()