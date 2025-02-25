n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!
dots_set = []

for i in range(1, n - 1):
    dots_set.append((x[:i] + x[i + 1:], y[:i] + y[i + 1:]))

min_length = float('inf')

for dots in dots_set:
    temp = 0
    for i in range(len(dots[0]) - 1):
        temp += abs(dots[0][i] - dots[0][i + 1]) + abs(dots[1][i] - dots[1][i + 1])
    min_length = min(min_length, temp)

print(min_length)