n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
count = c = 0

number = []

lines.sort(key=lambda x: x[0])

for i in range(n):
    for j in range(i + 1, n):
        if lines[i][1] > lines[j][1]:
            number.append(i)
            number.append(j)     

ns = set(number)

print(n - len(ns))