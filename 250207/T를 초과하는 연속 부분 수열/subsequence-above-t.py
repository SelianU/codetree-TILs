n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
count = 1
answer = 1
pos = 0

for i in range(len(arr)):
    if arr[i] > t:
        if i == 0 or arr[i] <= arr[pos]:
            count = 1
            pos = i
        else:
            count += 1
            pos += 1
    else:
        count = 0
        pos = i
    answer = max(count, answer)

print(answer)