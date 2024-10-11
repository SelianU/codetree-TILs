N = int(input())
li = []
for i in range(N):
    z = int(input())
    if z % 3 == 0:
        li.append(z)
for i in li:
    print(i)