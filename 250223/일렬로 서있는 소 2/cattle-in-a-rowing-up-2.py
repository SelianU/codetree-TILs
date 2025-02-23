N = int(input())
A = list(map(int, input().split()))

# Write your code here!
count = 0

for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if i < j < k and A[i] <= A[j] <= A[k]:
                count += 1

print(count)