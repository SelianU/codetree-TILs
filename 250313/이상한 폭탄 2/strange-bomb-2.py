N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
# 마지막 폭탄부터 N - 3번째 폭탄까지 순환한다
# 그 폭탄의 번호를 저장하고, 다음 K번째까지 순환한다.
# 순환하며 같은 번호의 폭탄이 있으면 값을 저장한다
answer = -1
for i in range(N - 1, K - 1, -1):
    bomb = num[i]
    for j in range(i - 1, i - K - 1, -1):
        if num[j] == bomb:
            answer = bomb
            break
    if answer != -1:
        break

print(answer)