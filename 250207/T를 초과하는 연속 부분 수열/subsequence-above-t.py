n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
count = 0
answer = 0
ar = []

for a in arr:
    if a > t:
        ar.append(a)

for i in range(len(ar)):
    if i == 0 or ar[i] <= ar[i - 1]:
        count = 1
    else:
        count += 1

    answer = max(answer, count)

print(answer)