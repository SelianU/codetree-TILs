n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
count = 0
answer = 0
pos = 0

for i in range(len(arr)):
    if arr[i] > t:
        if i == 0 or arr[i] <= arr[pos]:
            count = 1
        else:
            count += 1
            pos = i + 1

    answer = max(answer, count)

print(answer)