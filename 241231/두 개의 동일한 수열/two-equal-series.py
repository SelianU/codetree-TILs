n = int(input())

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

if sorted(li1) == sorted(li2):
    print("Yes")
else:
    print("No")