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
    line[p - 1] = candy[idx]

l = len(line)
answer = 0

for k in range(K, l - K):
    answer = max(answer, sum(line[k - K:k + K + 1]))

print(answer)
