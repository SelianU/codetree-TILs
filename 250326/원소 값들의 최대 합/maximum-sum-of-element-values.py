n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
def sumof(arr, idx, m):
    if m == 1:
        return arr[idx]
    return arr[idx] + sumof(arr, arr[idx], m - 1)

answer = 0
for i in range(1, len(arr)):
    temp = sumof(arr, i, m)
    answer = max(answer, temp)

print(answer)