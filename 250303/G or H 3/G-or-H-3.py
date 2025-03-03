n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
length = max(x) + 1
stamp = [0] * length
for idx, i in enumerate(x):
    stamp[i] = 1 if c[idx] == 'G' else 2

answer = 0
for i in range(length - k):
    answer = max(answer, sum(stamp[i:i + k + 1]))

print(answer)