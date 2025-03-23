n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def divide_x(points):
    points.sort(key = lambda x: x[0])
    length = len(points)
    if points[length // 2 - 1][0] != points[length // 2][0]:
        return points[length // 2][0] - 1
    elif points[length // 2 - 1][0] == points[length // 2][0] and points[length // 2][0] != points[length // 2 + 1][0]:
        return points[length // 2][0] + 1
    
def divide_y(points):
    points.sort(key = lambda y: y[1])
    length = len(points)
    if points[length // 2 - 1][1] != points[length // 2][1]:
        return points[length // 2][1] - 1
    elif points[length // 2 - 1][1] == points[length // 2][1] and points[length // 2][1] != points[length // 2 + 1][1]:
        return points[length // 2][1] + 1

def count_direction(x, y):
    count = [0, 0, 0, 0]
    for point in points:
        if check_first(x, y, point):
            count[0] += 1
        if check_second(x, y, point):
            count[1] += 1
        if check_third(x, y, point):
            count[2] += 1
        if check_fourth(x, y, point):
            count[3] += 1

    return max(count)

def check_first(x, y, point):
    if point[0] < x and point[1] > y:
        return True
def check_second(x, y, point):
    if point[0] > x and point[1] > y:
        return True
def check_third(x, y, point):
    if point[0] > x and point[1] < y:
        return True
def check_fourth(x, y, point):
    if point[0] < x and point[1] < y:
        return True

if __name__ == '__main__':
    x = divide_x(points)
    y = divide_y(points)
    count = count_direction(x, y)
    print(count)