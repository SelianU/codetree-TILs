n = int(input())

li = sorted(list(map(int, input().split())))

print(li[n] + li[n - 1])