def recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return recursive(n//3) + recursive(n - 1)

n = int(input())

print(recursive(n))