N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Write your code here!
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

direction = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

count = 0

for i in range(N):
    for j in range(dist[i]):
        x, y = x + dx[direction[dir[i]]], y + dy[direction[dir[i]]]
        # print(f"dist[i]: {dist[i]}, x: {x}, y: {y}, count: {count}")
        count += 1
        if x == 0 and y == 0:
            break
    if x == 0 and y == 0:
        break
    if i == N - 1:
        count = -1

print(count)