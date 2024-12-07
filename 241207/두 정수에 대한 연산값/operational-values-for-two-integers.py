def calc(a, b):
    if a > b:
        m = a + 25
        n = b * 2
    else:
        m = a * 2
        n = b + 25
    return m, n

a, b = map(int, input().split())

m, n = calc(a, b)

print(f"{m} {n}")