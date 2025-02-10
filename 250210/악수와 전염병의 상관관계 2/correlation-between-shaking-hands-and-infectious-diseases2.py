N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Write your code here!
people = {i:[0,0] for i in range(1, N + 1)}
people[P] = [1,0]

handshakes.sort(key=lambda x:x[0])

for handshake in handshakes:
    first, second = handshake[1], handshake[2]

    if people[first] == [0, 0]
        if people[second][1] < K and people[second][0] == 1:
            people[first] = [1, 0]
            people[second][1] += 1

    elif people[first] == [1, K]
        if people[second][1] < K and people[second][0] == 1:
            people[second][1] += 1

    elif people[first][1] < K and people[second] == [0, 0]:
        people[first][1] += 1
        people[second] = [1, 0]

    elif people[first][1] < K and people[second] == [1, K]:
        people[first][1] += 1
        
    else:
        people[first][1] += 1
        people[second][1] += 1
    
for person in people.items():
    print(person[1][0], end='')