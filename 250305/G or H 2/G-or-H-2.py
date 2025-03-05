n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
people.sort(key = lambda x : int(x[0]))
answer = 0

def check_single(line):
    s = True
    t = line[0][1]
    for l, a in line:
        if a != t:
            s = False
    if s:
        return int(line[-1][0]) - int(line[0][0])
    else: return 0

def check_same(line):
    g = h = 0
    for l, a in line:
        if a == 'G':
            g += 1
        else:
            h += 1
    if g == h:
        return int(line[-1][0]) - int(line[0][0])
    else:
        return 0

for i in range(n):
    for j in range(i + 1, n):
        temp = people[i:j + 1]
        same = check_same(temp)
        single = check_single(temp)
        answer = max(answer, same, single)

print(answer)
# line_length = max(pos) + 1
# line = [0] * line_length

# for idx, p in enumerate(pos):
#     if alpha[idx] == 'G':
#         line[p] = 1
#     else:
#         line[p] = 2

# def count_single(line):
#     count = 0
#     t = line[0]
#     answer = 0
#     for idx, dot in enumerate(line):
#         if idx == 0:
#             continue
#         if dot == t:
#             count += 1
#         else:
#             answer = max(answer, count)
#             count = 0
#             t = dot
    
#     return answer

# def count_same(line):
#     answer = 0
#     for i in range(line_length):
#         for j in range(i + 1, line_length):
#             temp = line[i:j + 1]
#             g = h = 0
#             if temp[-1] == 0 or temp[0] == 0:
#                 continue
#             for d in temp:
#                 if d == 1:
#                     g += 1
#                 elif d == 2:
#                     h += 1
#             if g == h:
#                 answer = max(answer, j - i)
    
#     return answer

# def max_picture_size(line):
#     if len(pos) == 1:
#         return 0

#     single = count_single(line)
#     same = count_same(line)

#     return max(single, same)    

# print(max_picture_size(line))