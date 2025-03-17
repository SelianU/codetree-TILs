n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
K = []

for i in range(n):
    for j in range(i + 1, n):
        if abs(a[i] - a[j]) < 2:
            continue
        if abs(a[i] - a[j]) % 2 == 0:
            K.append((a[i] + a[j]) // 2)

answer = 0
for i in (set(K)):
    answer = max(answer, K.count(i))
print(answer)