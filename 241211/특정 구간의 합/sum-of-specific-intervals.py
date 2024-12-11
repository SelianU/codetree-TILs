def add(a1, a2):
    global a
    return sum(a[a1 - 1:a2])

n, m = tuple(map(int, input().split()))

a = list(map(int, input().split()))

a1, a2 = [], []

for i in range(m):
    temp1, temp2 = map(int, input().split())
    a1.append(temp1)
    a2.append(temp2)

for i in range(m):
    print(add(a1[i], a2[i]))