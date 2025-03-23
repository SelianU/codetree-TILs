n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def divide(points, axis):
    points.sort(key = lambda x: x[axis])
    length = len(points)
    mid = length // 2

    if mid > 0 and points[mid - 1][axis] != points[mid][axis]:
        return (points[mid - 1][axis] + points[mid][axis]) // 2
    elif mid < length - 1 and points[mid][axis] != points[mid + 1][axis]:
        return (points[mid][axis] + points[mid + 1][axis]) // 2
    elif len(set(point[axis] for point in points)) == 1:
        return points[mid][axis] - 1
    return points[mid][axis]
    
def count_direction(x, y):
    count = [0, 0, 0, 0]
    for point in points:
        if point[0] < x and point[1] > y:
            count[0] += 1
        elif point[0] > x and point[1] > y:
            count[1] += 1
        elif point[0] > x and point[1] < y:
            count[2] += 1
        elif point[0] < x and point[1] < y:
            count[3] += 1
    return max(count)

if __name__ == '__main__':
    x = divide(points, 0)
    y = divide(points, 1)
    count = count_direction(x, y)
    print(count)