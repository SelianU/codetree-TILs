n = int(input())
sequence = list(map(int, input().split()))

# Write your code here!
class Position:
    def __init__(self, sequence, prePos, postPos):
        self.sequence = sequence
        self.prePos = prePos
        self.postPos = postPos

position = []

for i, j in enumerate(sequence):
    position.append(Position(j, i + 1, i + 1))

position.sort(key=lambda x:x.sequence)

for i in range(n):
    position[i].postPos = i + 1

position.sort(key=lambda x: x.prePos)

for i in range(n):
    print(position[i].postPos, end=' ')