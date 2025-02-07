n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
count = 0
answer = 0

for a in arr:
    if a > t:
        count += 1
    else:
        count = 0
    answer = max(answer, count)

print(answer)