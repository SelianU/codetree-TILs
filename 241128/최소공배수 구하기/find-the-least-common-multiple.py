n, m = map(int, input().split())

le = 1

for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        le = i

answer = n * m // le

print(answer)