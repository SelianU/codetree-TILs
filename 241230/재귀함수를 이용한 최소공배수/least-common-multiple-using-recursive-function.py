def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(n1, n2):
    return (n1 * n2) // gcd(n1, n2)

def recursive(li, n):
    if n == 1:
        return li[0]
    return lcm(li[n - 1], recursive(li, n - 1))

n = int(input())

li = list(map(int, input().split()))

print(recursive(li, n))