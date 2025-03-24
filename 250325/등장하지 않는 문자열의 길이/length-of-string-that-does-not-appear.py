N = int(input())
str = input()

# Please write your code here.
answer = 0
for i in range(1, N):
    count = False
    for j in range(N-i):
        temp = str[j:j + i]
        for k in range(j + 1, N - i + 1):
            sub = str[k:k + i]
            if temp == sub:
                count = True
                break
        if count:
            break
    if not count:
        answer = i
        break

print(answer)         