n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = float('inf')

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        temp = points[:i] + points[i + 1:]
        x1 = sorted(temp, key=lambda x:x[0])[0][0]
        x2 = sorted(temp, key=lambda x:x[0])[-1][0]
        y1 = sorted(temp, key=lambda x:x[1])[0][1]
        y2 = sorted(temp, key=lambda x:x[1])[-1][1]

        answer = min(answer, abs(x1 - x2) * abs(y1 - y2))

print(answer)