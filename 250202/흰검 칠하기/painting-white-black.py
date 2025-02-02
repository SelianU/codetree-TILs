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
                dots[pos] = [1, 'W', 1, 0]
            else:
                dots[pos][0] += 1
                dots[pos][1] = 'W'
                dots[pos][2] += 1
            pos -= 1
        pos += 1
    else:
        for j in range(x[i]):
            if pos not in dots:
                dots[pos] = [1, 'B', 0, 1]
            else:
                dots[pos][0] += 1
                dots[pos][1] = 'B'
                dots[pos][3] += 1
            pos += 1
        pos -= 1

answers = [0, 0, 0]
for dot in dots.values():
    if dot[0] == 0:
        continue
    elif dot[2] > 1 and dot[3] > 1:
        answers[2] += 1
    else:
        answers[0 if dot[1] == 'W' else 1] += 1

for answer in answers:
    print(answer, end=' ')