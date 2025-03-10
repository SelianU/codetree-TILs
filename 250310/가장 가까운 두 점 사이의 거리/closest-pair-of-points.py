n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = float('inf')

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        x1, y1 = points[i]
        x2, y2 = points[j]

        length = (x1 - x2) ** 2 + (y1 - y2) ** 2
        answer = min(answer, length)

print(answer)