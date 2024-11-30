def three_six_nine(n):
    while n != 0:
        k = n % 10
        if k == 3 or k == 6 or k == 9:
            return True
        n //= 10
    return False

def is_magic_number(n):
    return n % 3 == 0 or three_six_nine(n)

a, b = map(int, input().split())

cnt = 0

for i in range(a, b + 1):
    if is_magic_number(i):
        cnt += 1

print(cnt)