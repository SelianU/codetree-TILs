n = input()
k = input()

for i in k:
    if i == 'L':
        n = n[1:] + n[0]
    else:
        n = n[-1] + n[:-1]

print(n)