n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Write your code here!
RED = 1
BLUE = 2

area = [[0 for _ in range(201)] for _ in range(201)]

for i in range(n):
    for j in range(y1[i], y2[i]):
        for k in range(x1[i], x2[i]):
            if i % 2 == 0:
                area[j + 100][k + 100] = RED
            else:
                area[j + 100][k + 100] = BLUE

answer = 0
for i in area:
    for j in i:
        if j == BLUE:
            answer += 1

print(answer)