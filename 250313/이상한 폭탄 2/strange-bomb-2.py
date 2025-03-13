N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
answer = []

for i in range(N):
    for j in range(i + 1, N):
        if i + K < j:
            break
        if num[i] == num[j]:
            answer.append(num[i])
            
if not answer:
    print(-1)
else:
    print(max(answer))