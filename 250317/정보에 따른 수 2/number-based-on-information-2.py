T, a, b = map(int, input().split())
alpha_position = [tuple(input().split()) for _ in range(T)]

def near_N(position):
    d = float('inf')
    for ap in alpha_position:
        if ap[0] == 'N':
            d = min(d, abs(int(ap[1]) - position))
    return d

def near_S(position):
    d = float('inf')
    for ap in alpha_position:
        if ap[0] == 'S':
            d = min(d, abs(int(ap[1]) - position))
    return d

def special_position(position):
    d1 = near_S(position)
    d2 = near_N(position)
    if d1 <= d2:
        return True

answer = 0

for i in range(a, b + 1):
    if special_position(i):
        answer += 1

print(answer)