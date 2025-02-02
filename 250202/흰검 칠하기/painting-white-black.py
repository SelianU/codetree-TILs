n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Write your code here!
# dots = [[0, 'N'] for _ in range(100001)]

# k = 50001

# for i in range(n):
#     if dir[i] == 'L':
#         for j in range(x[i]):
#             dots[k][0] += 1
#             dots[k][1] = 'W'
#             k -= 1
#         k += 1
#     else:
#         for j in range(x[i]):
#             dots[k][0] += 1
#             dots[k][1] = 'B'
#             k += 1
#         k -= 1

# answers = [0, 0, 0]
# for dot in dots:
#     if dot[0] == 0:
#         continue
#     elif dot[0] > 3:
#         answers[2] += 1
#     elif dot[1] == 'W':
#         answers[0] += 1
#     else:
#         answers[1] += 1

# for answer in answers:
#     print(answer, end=' ')

dots = []
pos = 0
blank = True
for i in range(n):
    for j in range(x[i]):
        if not dots or pos < 0 or pos >= len(dots):
            if dir[i] == 'L':
                dot = [1, 'W']
                dots.insert(0, dot)
            elif dir[i] == 'R':
                dot = [1, 'B']
                dots.append(dot)
                pos += 1
        else: # 이미 있는 경우
            if dir[i] == 'L':
                dots[pos][0] += 1
                dots[pos][1] = 'W'
                pos -= 1
            elif dir[i] == 'R':
                dots[pos][0] += 1
                dots[pos][1] = 'B'
                pos += 1
        if x[i] - 1 == j and dir[i] == 'R':
            pos -= 1
        if x[i] - 1 == j and dir[i] == 'L':
            pos += 1
        if x[i] == 1 and blank:
            if dir[i] == 'R':
                pos += 1
            if dir[i] == 'L':
                pos -= 1
            blank = False

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