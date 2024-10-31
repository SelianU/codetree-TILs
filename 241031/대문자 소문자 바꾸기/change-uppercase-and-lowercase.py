n = input()

answer = ""

for i in n:
    if i < 'a':
        answer += i.lower()
    else:
        answer += i.upper()

print(answer)