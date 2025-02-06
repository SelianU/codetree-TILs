n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
answer = 0
for i in range(len(arr)):
    if i == 0 or arr[i] != arr[i - 1]:
        temp = 1
    else:
        temp += 1
    
    answer = max(temp, answer)
print(answer)