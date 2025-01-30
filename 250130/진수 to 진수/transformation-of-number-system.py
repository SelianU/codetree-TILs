a, b = map(int, input().split())
n = input()

# Write your code here!
def to_deca(a, num):
    answer = 0

    for i in num:
        answer = answer * a + int(i)
    return answer

def deca_to(b, num):
    n = []
    if num == 0:
        return 0

    while num > 0:
        n.append(num % b)
        num //= b

    return n[::-1]

def transfer(a, b, n):
    deca = to_deca(a, n)
    answer = deca_to(b, deca)
    return answer

ans = transfer(a, b, n)

for i in ans:
    print(i, end='')