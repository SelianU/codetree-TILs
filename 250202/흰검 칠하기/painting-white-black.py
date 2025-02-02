n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

dots = {}
pos = 0
for i in range(n):
    if dir[i] == 'L':
        for j in range(x[i]):
            if pos not in dots:
                dots[pos] = [1, 'W']
            else:
                dots[pos][0] += 1
                dots[pos][1] = 'W'
            pos -= 1
        pos += 1
    else:
        for j in range(x[i]):
            if pos not in dots:
                dots[pos] = [1, 'B']
            else:
                dots[pos][0] += 1
                dots[pos][1] = 'B'
            pos += 1
        pos -= 1

answers = [0, 0, 0]
for dot in dots.values():
    if dot[0] == 0:
        continue
    elif dot[0] > 3:
        answers[2] += 1
    elif dot[1] == 'W':
        answers[0] += 1
    else:
        answers[1] += 1

for answer in answers:
    print(answer, end=' ')