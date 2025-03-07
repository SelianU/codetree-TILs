n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
numbers = [str(i) for i in range(111, 1000) if '0' not in str(i)]
a = [str(i) for i in a]

count = 0
answer = 0

def compare(numb, comp):
    st = ba = 0
    pos = []
    for digit in range(3):
        if numb[digit] == comp[digit]:
            st += 1
            pos.append(digit)
    for digit in range(3):
        if digit not in pos and comp[digit] in numb:
            ba += 1
    return st, ba

for number in numbers:
    count = 0
    for i in range(n):
        strike, ball = compare(number, a[i])
        if strike == b[i] and ball == c[i]:
            count += 1
    if count == n:
        answer += 1

print(answer)