n = int(input())

i, cnt = 2, 1

while n > 1:
    n //= i
    i += 1
    cnt += 1

print(cnt)