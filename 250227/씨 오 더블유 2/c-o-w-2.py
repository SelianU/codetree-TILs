N = int(input())
cow = input()

c = o = answer = 0

idx = cow.index('C')

cow = cow[idx:]

for s in cow:
    if s == 'C':
        c += 1
    elif s == 'O':
        o += 1
    else:
        answer += c * o

print(answer)