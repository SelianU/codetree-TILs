N = int(input())
arr = [int(input()) for _ in range(N)]

# Write your code here!
length = 0
answer = 0
for i in range(len(arr)):
    if i == 0 or arr[i] / abs(arr[i]) != arr[i - 1] / abs(arr[i - 1]):
        length = 1
    else:
        length += 1
    answer = max(answer, length)

print(answer)