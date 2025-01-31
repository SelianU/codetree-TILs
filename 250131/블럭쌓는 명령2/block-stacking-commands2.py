n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Write your code here!
blocks = []
for _ in range(n):
    blocks.append(0)

for command in commands:
    for i in range(int(command[0]) - 1, int(command[1])):
        blocks[i] += 1

print(max(blocks))