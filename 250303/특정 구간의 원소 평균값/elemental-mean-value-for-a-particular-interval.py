n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
answer = 0

for i in range(n):
    for j in range(i, n):
        a = arr[i:j + 1]
        if sum(a) / len(a) in a:
            answer += 1

print(answer)