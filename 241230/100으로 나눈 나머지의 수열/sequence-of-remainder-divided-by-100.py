def recursive(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    return (recursive(n - 1) * recursive(n - 2)) % 100

n = int(input())

print(recursive(n))