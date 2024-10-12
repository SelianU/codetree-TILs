a, b = map(int, input().split())

cd = False

for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        cd = True
        break

if cd:
    print(1)
else:
    print(0)