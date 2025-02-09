n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Write your code here!
a = [0]
b = [0]

for i in range(n):
    for j in range(t[i]):
        if d[i] == 'L':
            a.append(a[-1] - 1)
        else:
            a.append(a[-1] + 1)

for i in range(m):
    for j in range(t_b[i]):
        if d_b[i] == 'L':
            b.append(b[-1] - 1)
        else:
            b.append(b[-1] + 1)

l_a = len(a) - 1
l_b = len(b) - 1

if l_a > l_b:
    maxlen = 'a'
else:
    maxlen = 'b'

count = 0

for i in range(1, max(l_a, l_b)):
    if maxlen == 'a':
        if i > l_b:
            if a[i - 1] != b[l_b] and a[i] == b[l_b]:
                count += 1
        else:
            if a[i - 1] != b[i - 1] and a[i] == b[i]:
                count += 1
    else:
        if i > l_a:
            if a[l_a] != b[i - 1] and a[l_a] == b[i]:
                count += 1
        else:
            if a[i - 1] != b[i - 1] and a[i] == b[i]:
                count += 1

print(count)