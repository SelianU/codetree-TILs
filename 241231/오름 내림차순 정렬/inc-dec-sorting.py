n = int(input())

li = list(map(int, input().split()))

li.sort()
for i in li:
    print(f"{i}", end=' ')
print()
li.reverse()
for i in li:
    print(f"{i}", end=' ')