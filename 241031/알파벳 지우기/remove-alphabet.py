n = input()
m = input()

answer = ""
temp = ""

for k in n:
    if k < 'A':
        answer += k

for k in m:
    if k < 'A':
        temp += k

print(int(answer) + int(temp))