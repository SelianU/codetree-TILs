n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Write your code here!
a, b = [0], [0]

apos, bpos = 0, 0

for i in range(n):
    for j in range(t[i]):
        if d[i] == 'R':
            apos += 1
        else:
            apos -= 1
        a.append(apos)

for i in range(m):
    for j in range(t2[i]):
        if d2[i] == 'R':
            bpos += 1
        else:
            bpos -= 1
        b.append(bpos)

answer = 0

for i in range(1, len(a)):
    if a[i] == b[i]:
        answer = i
        break

if answer == 0:
    print(-1)
else:
    print(answer)