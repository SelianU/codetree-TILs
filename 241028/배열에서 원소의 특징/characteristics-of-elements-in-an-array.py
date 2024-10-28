li = list(map(int, input().split()))
for i in range(len(li)):
    if li[i]%3==0:
        print(li[i-1])
        break