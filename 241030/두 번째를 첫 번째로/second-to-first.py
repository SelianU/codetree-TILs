n = input()

k = n[0]
answer = ""

for i, j in enumerate(n):
    if i % 2 == 1:
        answer += k
    else:
        answer += n[i]

print(answer)