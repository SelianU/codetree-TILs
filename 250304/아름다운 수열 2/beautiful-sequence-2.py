N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
answer = 0

for i in range(N - M + 1):
    count = 0
    for b in B:
        if b in A[i:i + M]:
            count += 1
    if count == M:
        answer += 1

print(answer)