n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
dots = [0 for _ in range(100)]

for segment in segments:
    for i in range(int(segment[0]) - 1, int(segment[1])):
        dots[i] += 1

print(max(dots))