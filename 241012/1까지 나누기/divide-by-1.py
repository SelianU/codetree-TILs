n = int(input())

i, cnt = 2, -1

while n != 0:
    n //= i
    cnt += 1

print(cnt)