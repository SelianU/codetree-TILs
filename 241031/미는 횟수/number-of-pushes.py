n = input()
m = input()

count = 0

for i in range(len(n) + 1):
    if n == m:
        break
    count += 1
    n = n[-1] + n[:-1]
    if i == len(n):
        count = -1

print(len(n) if count == 0 else count)