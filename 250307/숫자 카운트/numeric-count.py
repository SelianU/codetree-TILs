n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
numbers = [str(i) for i in range(111, 1000) if '0' not in str(i) and str(i)[0] != str(i)[1] and str(i)[1] != str(i)[2] and str(i)[0] != str(i)[2]]
a = [str(i) for i in a]

count = 0
answer = 0

def countStrike(numb, comp):
    k = 0
    for l in range(3):
        if numb[l] == comp[l]:
            k += 1
    return k

def countBall(numb, comp):
    k = 0
    for l in range(3):
        if numb[l] != comp[l] and numb[l] in comp:
            k += 1
    return k

def compare(numb, comp):
    return countStrike(numb, comp), countBall(numb, comp)

for number in numbers:
    count = 0
    for i in range(n):
        strike, ball = compare(number, a[i])
        if strike == b[i] and ball == c[i]:
            count += 1
    if count == n:
        answer += 1

print(answer)