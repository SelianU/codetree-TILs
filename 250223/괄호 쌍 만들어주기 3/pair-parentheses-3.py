A = input()

# Write your code here!
count = 0

for idx, a in enumerate(A):
    if a == ')':
        continue
    for j in range(idx, len(A)):
        if A[j] == ')':
            count += 1

print(count)