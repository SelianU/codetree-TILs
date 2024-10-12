n = int(input())

i, cnt = 2, 1

while n != 0:
    n //= i
    i += 1
    cnt += 1

print(cnt)