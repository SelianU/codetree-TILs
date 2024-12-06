def calc_li(length, li):
    for i in range(length):
        if li[i] % 2 == 0:
            li[i] //= 2

n = int(input())

_li = list(map(int, input().split()))

calc_li(n, _li)

for i in _li:
    print(i, end=' ')