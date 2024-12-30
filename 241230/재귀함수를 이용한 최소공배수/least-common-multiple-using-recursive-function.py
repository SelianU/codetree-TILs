def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(n1, n2):
    return (n1 * n2) / gcd(n1, n2)

def recursive(li):
    if len(li) == 2:
        return lcm(li[0], li[1])
    return lcm(recursive(li[:-1]), li[-1])

n = int(input())

li = list(map(int, input().split()))

print(int(recursive(li)))