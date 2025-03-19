n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.
# 해수면의 높이를 하나씩 높이면서 덩어리의 수를 구해 answer에 넣는다
height = max(h) - 1
answer = 0

for i in range(height):
    h = [ice - 1 if ice > 1 else 0 for ice in h]
    count = 0
    for k in range(len(h)):
        if 0 in h and h[0] == 0:
            h.remove(0)
        else:
            break
    for idx in range(len(h) - 1):
        if h[idx] == 0 and h[idx + 1] != 0:
            count += 1
    answer = max(count, answer)

print(answer + 1)