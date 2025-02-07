n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
count = 1
answer = 1

for i in range(len(arr)):
    if i == 0 or arr[i] <= arr[i - 1]:
        count = 1
    else:
        count += 1
    answer = max(count, answer)

print(answer)