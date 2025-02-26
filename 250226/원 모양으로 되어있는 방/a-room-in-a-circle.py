N = int(input())

rooms = [int(input()) for _ in range(N)]

answer = float('inf')

for start_room in range(N):
    length = 0
    for i in range(N):
        pos = (start_room + i) % N
        length += rooms[pos] * i
    answer = min(length, answer)

print(answer)