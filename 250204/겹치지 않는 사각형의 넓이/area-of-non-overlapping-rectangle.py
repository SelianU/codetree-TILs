x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Write your code here!
area = [[0 for _ in range(1000)] for _ in range(1000)]

for i in range(2):
    for x in range(x1[i], x2[i]):
        for y in range(y1[i], y2[i]):
            area[y + 500][x + 500] = 1

for x in range(x1[2], x2[2]):
        for y in range(y1[2], y2[2]):
            area[y + 500][x + 500] = 0

answer = 0

for i in area:
    for j in i:
        if j == 1:
            answer += 1

print(answer)