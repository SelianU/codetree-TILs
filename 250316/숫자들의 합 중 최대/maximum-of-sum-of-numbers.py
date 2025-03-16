X, Y = map(int, input().split())

# Please write your code here.
answer = 0
for number in range(X, Y + 1):
    temp = 0
    for n in str(number):
        temp += int(n)
    answer = max(temp, answer)

print(answer)