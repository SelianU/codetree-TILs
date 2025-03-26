n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
def sumof(arr, idx, m):
    tot = 0
    t = idx
    for k in range(m):
        t = arr[t]
        tot += t
    return tot

answer = 0
for i in range(1, len(arr)):
    temp = sumof(arr, i, m)
    answer = max(answer, temp)

print(answer)