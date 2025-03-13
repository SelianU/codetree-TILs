N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
answer = -1

for i in range(N - 1, K - 2, -1):
    bomb = num[i]
    for j in range(i - 1, i - K - 2, -1):
        if num[j] == bomb:
            answer = bomb
            break
    if answer != -1:
        break

print(answer)