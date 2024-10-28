n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

sums = []

for k in li:
    add = 0
    for i in range(k[0], k[1] + 1):
        if i % 2 == 0:
            add += i
    sums.append(add)

for k in sums:
    print(k)