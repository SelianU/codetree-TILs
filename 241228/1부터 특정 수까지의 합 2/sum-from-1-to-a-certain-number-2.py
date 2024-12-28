def recursive_sum(n):
    if n == 1:
        return 1
    return recursive_sum(n - 1) + n

n = int(input())

print(recursive_sum(n))