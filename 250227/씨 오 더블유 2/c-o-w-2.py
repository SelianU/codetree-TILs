N = int(input())
cows = input()
answer = 0

for idx, c in enumerate(cows):
    if c == 'C':
        for id in range(idx, len(cows)):
            if cows[id] == 'O':
                for i in range(id, len(cows)):
                    if cows[i] == 'W':
                        answer += 1

print(answer)