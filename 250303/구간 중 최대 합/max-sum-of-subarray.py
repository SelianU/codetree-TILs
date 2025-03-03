n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_sum = 0
for i in range(n - k + 1):
    max_sum = max(sum(arr[i:i + k]), max_sum)

print(max_sum)