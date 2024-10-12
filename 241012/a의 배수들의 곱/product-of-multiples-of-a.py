a, b = map(int, input().split())

mul = 1

for i in range(a, b + 1, a):
    mul *= i

print(mul)