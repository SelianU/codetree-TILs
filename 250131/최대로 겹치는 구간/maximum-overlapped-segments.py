n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
dots = [0 for _ in range(201)]

for segment in segments:
    for i in range(int(segment[0]) + 100, int(segment[1]) + 100):
        dots[i] += 1

print(max(dots))