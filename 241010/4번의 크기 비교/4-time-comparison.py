a = int(input())
li = list(map(int, input().split()))

for i in li:
    if a > i:
        print(1)
    else:
        print(0)