a, b = map(int, input().split())

m = [0] * 10

while a > 1:
    m[a % b] += 1
    a //= b

answer = 0

for i in m:
    answer += i * i

print(answer)