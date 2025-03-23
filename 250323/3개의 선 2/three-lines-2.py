n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def choose_3_and_delete_column(p_x, points):
    for i_idx, first in enumerate(p_x):
        for j_idx, second in enumerate(p_x):
            for k_idx, third in enumerate(p_x):
                # p에 있는 거 제외하고 남은거 묶어서 리스트로 만들어
                p = [point for point in points if point[0] != first and point[0] != second and point[0] != third]
                if not p:
                    continue
                else:
                    return True
    return False

def choose_3_and_delete_row(p_y, points):
    for i_idx, first in enumerate(p_y):
        for j_idx, second in enumerate(p_y):
            for k_idx, third in enumerate(p_y):
                # p에 있는 거 제외하고 남은거 묶어서 리스트로 만들어
                p = [point for point in points if point[1] != first and point[1] != second and point[1] != third]
                if not p:
                    continue
                else:
                    return True
    return False

def choose_2_1_and_delete(p_x, p_y, points):
    for i_idx, first in enumerate(p_x):
        for j_idx, second in enumerate(p_x):
            for k_idx, third in enumerate(p_y):
                # p에 있는 거 제외하고 남은거 묶어서 리스트로 만들어
                p = [point for point in points if point[0] != first and point[0] != second and point[1] != third]
                if not p:
                    continue
                else:
                    return True
    return False

def choose_1_2_and_delete(p_x, p_y, points):
    for i_idx, first in enumerate(p_x):
        for j_idx, second in enumerate(p_y):
            for k_idx, third in enumerate(p_y):
                # p에 있는 거 제외하고 남은거 묶어서 리스트로 만들어
                p = [point for point in points if point[0] != first and point[1] != second and point[1] != third]
                if not p:
                    continue
                else:
                    return True
    return False


p_x = set(point[0] for point in points)
p_y = set(point[1] for point in points)

if choose_3_and_delete_column(p_x, points):
    print(1)
elif choose_3_and_delete_row(p_y, points):
    print(1)
elif choose_2_1_and_delete(p_x, p_y, points):
    print(1)
elif choose_1_2_and_delete(p_x, p_y, points):
    print(1)
else:
    print(0)