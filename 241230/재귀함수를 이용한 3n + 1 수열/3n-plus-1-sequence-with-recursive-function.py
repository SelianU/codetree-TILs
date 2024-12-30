def recursive(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    return recursive(n) + 1

n = int(input())

print(recursive(n))