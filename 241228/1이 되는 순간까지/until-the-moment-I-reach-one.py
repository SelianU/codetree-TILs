def recursive_count(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return recursive_count(n // 2) + 1
    else:
        return recursive_count(n // 3) + 1

n = int(input())

print(recursive_count(n))