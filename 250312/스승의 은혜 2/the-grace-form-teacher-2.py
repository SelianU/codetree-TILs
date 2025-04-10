N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
P.sort()
answer = 0

for i in range(N + 1): # 반값
    for j in range(i + 1, N + 1):
        P_temp = P[:i] + [P[i] // 2] + P[i + 1:j]
        if sum(P_temp) <= B:
            answer = max(answer, j)
        else:
            continue

print(answer)