def mul(a, b, c):
    return a * b * c

def recursive_sum(n):
    if n < 10:
        return n
    return recursive_sum(n // 10) + n % 10

a, b, c = map(int, input().split())

print(recursive_sum(mul(a, b, c)))