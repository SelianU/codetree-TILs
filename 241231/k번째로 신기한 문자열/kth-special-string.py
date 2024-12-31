n, k, T = input().split()
n, k = int(n), int(k)

li = [input() for i in range(n)]
li_ = []
for i in li:
    if T in i[:len(T)]:
        li_.append(i)

print(sorted(li_)[k - 1])