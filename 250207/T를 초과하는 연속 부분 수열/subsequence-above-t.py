n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
count = 0
answer = 0

for i in range(len(arr)):
    if arr[i] > t:
        if i == 0 or arr[i] <= arr[i - 1]:
            count = 1
        else:
            count += 1
    elif count > 0:
        count = 0
    answer = max(answer, count)

print(answer)