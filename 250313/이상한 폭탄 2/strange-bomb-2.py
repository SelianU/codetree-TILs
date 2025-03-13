N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
answer = []

for i in range(N - 1, K - 2, -1):
    for j in range(i - 1, i - K - 2, -1):
        if num[j] == num[i]:
            answer.append(num[i])

if not answer:
    print(-1)
else:
    print(max(answer))