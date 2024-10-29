n, m = map(int, input().split())
li_1 = [list(map(int, input().split())) for _ in range(n)]
li_2 = [list(map(int, input().split())) for _ in range(n)]
answer = []
for p, q in enumerate(li_1):
    sub_list = []
    for r, s in enumerate(q):
        if li_2[p][r] != s:
            sub_list.append(1)
        else:
            sub_list.append(0)
    answer.append(sub_list)

for i in answer:
    for j in i:
        print(j, end=' ')
    print()