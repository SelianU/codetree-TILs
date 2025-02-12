dirs = input()

# Write your code here!
x, y = 0, 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

direction = 0

for dir in dirs:
    if dir == 'F':
        x += dx[direction]
        y += dy[direction]
    elif dir == 'R':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4

print(f"{x} {y}")