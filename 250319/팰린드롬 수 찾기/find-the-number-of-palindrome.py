X, Y = map(int, input().split())

# Please write your code here.
def check_pelindrom(number):
    number = str(number)
    num_len = len(number)
    num1 = number[:num_len // 2]
    if num_len % 2 == 0:
        num2 = number[num_len // 2:][::-1]
    else:
        num2 = number[num_len // 2 + 1:][::-1]
    if num1 == num2: return True
    else: False

answer = 0
for i in range(X, Y + 1):
    if check_pelindrom(i):
        answer += 1

print(answer)