n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def divide_x(points):
    points.sort(key = lambda x: x[0])
    length = len(points)
    mid = length // 2
    if points[mid - 1][0] != points[mid][0]:
        return points[mid][0] - 1
    elif points[mid - 1][0] == points[mid][0] and points[mid][0] != points[mid + 1][0]:
        return points[mid][0] + 1
    else:
        return points[mid][0] - 1
    
def divide_y(points):
    points.sort(key = lambda y: y[1])
    length = len(points)
    mid = length // 2
    if points[mid - 1][1] != points[mid][1]:
        return points[mid][1] - 1
    elif points[mid - 1][1] == points[mid][1] and points[mid][1] != points[mid + 1][1]:
        return points[mid][1] + 1
    else:
        return points[mid][1] - 1

def count_direction(x, y):
    count = [0, 0, 0, 0]
    for point in points:
        if point[0] < x and point[1] > y:
            count[0] += 1
        if point[0] > x and point[1] > y:
            count[1] += 1
        if point[0] > x and point[1] < y:
            count[2] += 1
        if point[0] < x and point[1] < y:
            count[3] += 1
    return max(count)

if __name__ == '__main__':
    x = divide_x(points)
    y = divide_y(points)
    count = count_direction(x, y)
    print(count)