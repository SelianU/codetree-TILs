def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_sum_even_number(k):
    add = 0
    while k > 0:
        add += k % 10
        k //= 10
    return True if add % 2 == 0 else False

def is_magic_number(n):
    if is_prime_number(n) and is_sum_even_number(n):
        return True
    return False

def count_magic_number(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if is_magic_number(i):
            cnt += 1
    return cnt

a, b = map(int, input().split())

answer = count_magic_number(a, b)

print(answer)