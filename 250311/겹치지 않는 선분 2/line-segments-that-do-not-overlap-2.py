n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0

for i in range(n):
    count = 0
    for j in range(i + 1, n):
        if lines[i][0] < lines[j][0] and lines[i][1] < lines[j][1]: # not cross
            continue
        count += 1
    if count == 0:
        answer += 1

print(answer)