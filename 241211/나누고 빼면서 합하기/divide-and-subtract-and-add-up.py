def calc(li, m):
    if m == 1:
        return li[0]
    else:
        temp = m
        m = m // 2 if m % 2 == 0 else m - 1
        return li[temp - 1] + calc(li, m)

n, m = map(int, input().split())

li = list(map(int, input().split()))

answer = calc(li, m)

print(answer)