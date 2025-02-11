N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Write your code here!
HoF = 0

a = [0]
b = [0]

for i in range(N):
    for _ in range(t[i]):
        a.append(a[-1] + v[i])

for j in range(M):
    for _ in range(t2[j]):
        b.append(b[-1] + v2[j])

for i in range(1, len(a)):
    if a[i] > b[i] and a[i - 1] <= b[i - 1]:
        HoF += 1
    elif a[i] == b[i] and a[i - 1] != b[i - 1]:
        HoF += 1
    elif a[i] < b[i] and a[i - 1] >= b[i - 1]:
        HoF += 1

print(HoF)