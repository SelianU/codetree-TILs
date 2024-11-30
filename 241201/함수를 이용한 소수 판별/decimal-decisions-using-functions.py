def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def add_prime(a, b):
    prime = 0
    for i in range(a, b + 1):
        if is_prime(i):
            prime += i

    return prime

a, b = map(int, input().split())

answer = add_prime(a, b)

print(answer)