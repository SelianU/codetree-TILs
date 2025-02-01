n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Write your code here!
dots = [0 for _ in range(201)]

k = 101

for i in range(n):
    for j in range(x[i]):
        if dir[i] == 'L':
            k -= 1
            dots[k] += 1
        if dir[i] == 'R':
            dots[k] += 1
            k += 1

answer = 0
for dot in dots:
    if dot > 1:
        answer += 1
print(answer)