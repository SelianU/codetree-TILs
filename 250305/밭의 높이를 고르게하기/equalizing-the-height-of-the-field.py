N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
t = []
for a in arr:
    t.append(abs(a - H))

answer = float('inf')

for i in range(N - T + 1):
    answer = min(sum(t[i:i + T]), answer)

print(answer)