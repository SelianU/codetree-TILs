n, m = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(m)]

answer = [[0 for _ in range(n)] for _ in range(n)]

for k in li:
    answer[k[0]-1][k[1]-1]=k[0]*k[1]

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()