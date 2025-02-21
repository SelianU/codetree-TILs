n = int(input())
A = list(map(int, input().split()))

# Write your code here!
min_sum = 1000000000
for i in range(n):
    temp = 0
    for j in range(n):
        temp += A[j] * abs(j - i)
    min_sum = min(min_sum, temp)

print(min_sum)