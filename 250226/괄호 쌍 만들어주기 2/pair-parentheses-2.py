A = input()
count = 0
answer = 0

for i in range(len(A)):
    if A[i:i + 2] == '((':
        count += 1
    elif A[i:i + 2] == '))':
        answer += count

print(answer)