commands = input()

# Write your code here!
x, y = 0, 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

dir = 0

count = 0

for command in commands:
    if command == 'F':
        x, y = x + dx[dir], y + dy[dir]
    elif command == 'R':
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4
    count += 1
    if x == 0 and y == 0:
        break
    
if count == len(commands) and (x != 0 or y != 0):count = -1

print(count)
