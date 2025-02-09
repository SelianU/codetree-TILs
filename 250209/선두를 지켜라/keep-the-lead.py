n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Write your code here!
a = [0]
b = [0]

for i in range(n):
    for j in range(t[i]):
        a.append(a[-1] + v[i])

for i in range(m):
    for j in range(t2[i]):
        b.append(b[-1] + v2[i])

change = 0

if a[1] > b[1]:
    first, second = a, b
else:
    first, second = b, a

for idx in range(2, len(a)):
    if first[idx] < second[idx]:
        first, second = second, first
        change += 1

print(change)