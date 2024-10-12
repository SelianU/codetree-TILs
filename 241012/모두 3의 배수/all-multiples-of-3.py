li = []

for _ in range(5):
    li.append(int(input()))

li = [i % 3 for i in li]

if 1 in li or 2 in li:
    print(0)
else:
    print(1)