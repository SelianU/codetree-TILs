X, Y = map(int, input().split())

# Please write your code here.
answer = 0

def interestingNumber(num):
    num = str(num)
    set_num = set(num)
    if len(set_num) == 2:
        for k in set_num:
            count = 0
            for j in num:
                if j == k:
                    count += 1
            if count == 1:
                return True
    return False

for i in range(X, Y + 1):
    if interestingNumber(i):
        answer += 1

print(answer)