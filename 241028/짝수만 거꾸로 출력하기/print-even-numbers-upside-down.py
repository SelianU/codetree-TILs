n = int(input())

li = list(map(int, input().split()))

li_even = []

for k in li:
    if k % 2 == 0: li_even.append(k)
    
for k in li_even[::-1]:
    print(k, end=' ')