N = int(input())
seat = input()

# Please write your code here.
answer = 0
for i in range(len(seat)):
    if seat[i] == '1':
        continue
    else:
        s = seat[:i] + '1' + seat[i + 1:]
        pos = []
        for idx, a in enumerate(s):
            if a == '1':
                pos.append(idx)
        t = []
        for j in range(len(pos) - 1):
            t.append(pos[j + 1] - pos[j])
        answer = max(min(t), answer)

print(answer)