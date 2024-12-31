n = int(input())

li = list(map(int, input().split()))

li_ = []

for i in range(len(li)):
    li_.append(li[i])
    li_.sort()
    
    if i % 2 == 0:
        print(li_[(i + 1) // 2], end=' ')