n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
line_length = max(pos) + 1
line = [0] * line_length

for idx, p in enumerate(pos):
    if alpha[idx] == 'G':
        line[p] = 1
    else:
        line[p] = 2

def count_single(line):
    count = 0
    t = line[0]
    answer = 0
    for idx, dot in enumerate(line):
        if idx == 0:
            continue
        if dot == t:
            count += 1
        else:
            answer = max(answer, count)
            count = 0
            t = dot
    
    return answer

def count_same(line):
    answer = 0
    for i in range(line_length):
        for j in range(i + 1, line_length):
            temp = line[i:j + 1]
            g = h = 0
            if temp[-1] == 0 or temp[0] == 0:
                continue
            for d in temp:
                if d == 1:
                    g += 1
                elif d == 2:
                    h += 1
            if g == h:
                answer = max(answer, j - i)
    
    return answer

def max_picture_size(line):
    if len(pos) == 1:
        return 0

    single = count_single(line)
    same = count_same(line)

    return max(single, same)    

print(max_picture_size(line))