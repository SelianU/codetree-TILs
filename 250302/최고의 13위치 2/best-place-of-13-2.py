n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0

for i in range(n):
    for j in range(i, n):
        for ii in range(n - 2):
            for jj in range(n - 2):
                if i == j:
                    if n < 6:
                        break
                    elif ii + 2 < jj:
                        answer = max(answer, sum(arr[i][ii:ii + 3]) + sum(arr[j][jj:jj + 3]))
                else:
                    answer = max(answer, sum(arr[i][ii:ii + 3]) + sum(arr[j][jj:jj + 3]))

print(answer)