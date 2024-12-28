def recursive_square(n):
    if n < 10:
        return n ** 2
    
    return recursive_square(n // 10) + (n % 10) ** 2

n = int(input())

print(recursive_square(n))