N = int(input())
seat = input()

# Please write your code here.
max_blank = 0
for s in seat:
    if s == '0':
        count += 1
    else:
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

print(answer)