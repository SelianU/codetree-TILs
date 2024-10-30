n = input()

k = n[0]
a = n[1]
answer = ""

for i, j in enumerate(n):
    if n[i] == a:
        answer += k
    else:
        answer += n[i]

print(answer)