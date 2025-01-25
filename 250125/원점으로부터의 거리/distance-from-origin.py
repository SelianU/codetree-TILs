n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Write your code here!

def length(x, y):
    return abs(x) + abs(y)

lengths = [length(points[i][1][0], points[i][1][1]) for i in range(n)]

man = [(points[i], lengths[i]) for i in range(n)]

man.sort(key=lambda x: (x[1], x[0][0]))

for i in range(n):
    print(man[i][0][0] + 1)