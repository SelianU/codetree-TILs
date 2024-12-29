def recursive_max(li):
    if not li:
        return 1
    temp = recursive_max(li[:-1])
    return temp if temp > li[-1] else li[-1]

n = int(input())

li = list(map(int, input().split()))

print(recursive_max(li))