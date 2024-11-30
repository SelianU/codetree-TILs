def is_magic_number(n):
    temp = 0
    if n % 2 == 0:
        while n != 0:
            temp += n % 10
            n //= 10
        if temp % 5 == 0:
            return True
    return False

n = int(input())

if is_magic_number(n):
    print("Yes")
else:
    print("No")