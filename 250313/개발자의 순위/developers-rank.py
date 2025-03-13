k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
# 1번째 경기에서 순위 추출
# 이후 경기마다 순위 비교
# k번인 짝의 수
dev_levels = []
for i in range(n):
    for j in range(i + 1, n):
        dev_levels.append((arr[0][i], arr[0][j]))

levels = [0] * len(dev_levels)

for i in range(1, k):
    for j in range(len(dev_levels)):
        if arr[i].index(dev_levels[j][0]) < arr[i].index(dev_levels[j][1]):
            levels[j] += 1

sets = 0
for i in levels:
    if i == k - 1:
        sets += 1

print(sets)