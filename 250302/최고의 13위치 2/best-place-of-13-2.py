n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

answer = 0

for i in range(n):
    for j in range(i + 1, n):
        for ii in range(n - 2):
            for jj in range(n - 2):
                answer = max(answer, sum(arr[i][ii:ii + 3]) + sum(arr[j][jj:jj + 3]))

print(answer)