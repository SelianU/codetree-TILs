N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
line = [0] * max(pos)

for idx, p in enumerate(pos):
    line[p - 1] += candy[idx]

l = len(line)
answer = 0

for k in range(l):
    ad = 0
    ov = 0
    if k - K < 0:
        ad = abs(k - K)
    if k + K + 1 > l:
        ov = k + K + 1 - l
    answer = max(answer, sum(line[k - K + ad:k + K + 1 - ov]))

print(answer)
