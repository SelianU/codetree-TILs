N = int(input())
seat = input()

# Please write your code here.
max_blank = 0
min_blank = float('inf')

for s in range(len(seat)):
    if seat[s] == '0':
        count += 1
    else:
        if s != 0:
            min_blank = min(min_blank, count)
        count = 0
    max_blank = max(max_blank, count)
    
if count != 0:
    last_blank = count


answer = 0
if max_blank % 2 == 1:
    answer = max_blank // 2 + 1
else:
    answer = max_blank // 2

answer = max(answer, last_blank)

answer = min(answer, min_blank + 1)

print(answer)