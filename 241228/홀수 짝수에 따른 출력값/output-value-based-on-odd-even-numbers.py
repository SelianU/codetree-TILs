def recursive_sum(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return recursive_sum(n - 2) + n

n = int(input())

print(recursive_sum(n))