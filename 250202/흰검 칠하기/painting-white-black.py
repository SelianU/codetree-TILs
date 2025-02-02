n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Write your code here!
dots = [[0, 'N'] for _ in range(201)]

k = 101

for i in range(n):
    if dir[i] == 'L':
        for j in range(x[i]):
            dots[k][0] += 1
            dots[k][1] = 'W'
            k -= 1
        k += 1
    else:
        for j in range(x[i]):
            dots[k][0] += 1
            dots[k][1] = 'B'
            k += 1
        k -= 1

answers = [0, 0, 0]
for dot in dots:
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