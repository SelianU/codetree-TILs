n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Write your code here!
area = [[0 for _ in range(200)] for _ in range(200)]

for i in range(n):
    for x in range(x1[i], x2[i]):
        for y in range(y1[i], y2[i]):
            area[y + 100][x + 100] = 1

answer = 0

for i in area:
    for j in i:
        if j == 1:
            answer += 1

print(answer)