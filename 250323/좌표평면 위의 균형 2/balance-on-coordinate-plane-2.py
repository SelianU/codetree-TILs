n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

dots = float('inf')
for x in range(2, 100, 2):
    for y in range(2, 100, 2):
        p = [0, 0, 0, 0]
        for point in points:
            if point[0] < x and point[1] < y:
                p[0] += 1
            elif point[0] < x and point[1] > y:
                p[1] += 1
            elif point[0] > x and point[1] < y:
                p[2] += 1
            elif point[0] > x and point[1] > y:
                p[3] += 1
        dot = max(p)
        dots = min(dot, dots)

print(dots)