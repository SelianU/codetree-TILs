N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
data = []

def in_range(temperature, temp_range):
    if temperature < temp_range[0]:
        return C
    elif temperature <= temp_range[1]:
        return G
    else:
        return H

for i in range(1001):
    work = 0
    for _range in ranges:
        work += in_range(i, _range)
    data.append(work)

print(max(data))