n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
heights = []

for i in range(n):
    for j in range(i + 1, n):
        if points[i][0] == points[j][0]:
            height = abs(points[i][1] - points[j][1])
            x1 = points[i]
            x2 = points[j]
            heights.append((height, x1, x2))

areas = []

for height in heights:
    dot1 = height[1]
    dot2 = height[2]
    for i in range(n):
        if points[i][1] == dot1[1]:
            areas.append(height[0] * abs(dot1[0] - points[i][0]))
        if points[i][1] == dot2[1]:
            areas.append(height[0] * abs(dot1[0] - points[i][0]))

print(max(areas))