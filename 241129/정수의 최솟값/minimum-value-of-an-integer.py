def minimum(*args):
    return min(args)


a, b, c = tuple(map(int, input().split()))

print(minimum(a, b, c))