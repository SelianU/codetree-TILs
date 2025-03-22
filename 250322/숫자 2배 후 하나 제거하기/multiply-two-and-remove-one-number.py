n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
answer = float('inf')
for i in range(n):
    for j in range(n):
        temp = arr[:]
        temp[i] *= 2
        temp = temp[:j] + temp[j + 1:]
        sub = 0
        for k in range(n - 2):
            sub += abs(temp[k] - temp[k + 1])
        answer = min(sub, answer)

print(answer)