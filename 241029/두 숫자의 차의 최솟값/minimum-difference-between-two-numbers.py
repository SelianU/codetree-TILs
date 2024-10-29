n = int(input())

li = list(map(int, input().split()))

answer = li[1]-li[0]

for i in range(len(li)-1):
    for j in range(i + 1, len(li)):
        answer = min(answer, li[j]-li[i])

print(answer)