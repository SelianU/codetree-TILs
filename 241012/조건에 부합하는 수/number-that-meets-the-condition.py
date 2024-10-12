a = int(input())

li = []

for i in range(a, 0, -1):
    if i % 2 == 0 and i % 4 != 0:
        continue
    if (i // 8) % 2 == 0:
        continue
    if i % 7 < 4:
        continue
    li.append(i)
li.sort()

for i in li:
    print(i, end=' ')