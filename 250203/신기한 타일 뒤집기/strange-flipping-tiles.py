n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Write your code here!
dots = {}
pos = 0

for i in range(n):
    if dir[i] == 'L':
        for j in range(x[i]):
            dots[pos] = 'W'
            pos -= 1
        pos += 1
    else:
        for j in range(x[i]):
            dots[pos] = 'B'
            pos += 1
        pos -= 1

answers = [0, 0]

for k in dots.values():
    if k == 'W':
        answers[0] += 1
    else:
        answers[1] += 1

for i in answers:
    print(i, end=' ')