a, b = map(int, input().split())

m = [0] * 10

while a != 0:
    m[a % b] += 1
    a //= b

answer = 0

for i in m:
    answer += i ^ 2

print(answer)