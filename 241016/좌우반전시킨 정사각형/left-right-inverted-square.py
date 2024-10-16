n = int(input())
li=[]

for i in range(n, 0, -1):
    li.append(i)

answer = []
for i in range(1, n + 1):
    answer.append([i * j for j in li])

for i in answer:
    for j in i:
        print(j,end=' ')
    print()