n = int(input())

li = sorted(list(map(int, input().split())))
li_ = [li[i] + li[2 * n - i - 1] for i in range(n)]
print(max(li_))