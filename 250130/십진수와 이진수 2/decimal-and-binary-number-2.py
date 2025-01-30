N = input()

# Write your code here!
def digit_to_Deca(num):
    n = 0
    for i in num:
        n = n * 2 + int(i)
    return n

def deca_to_Digit(num):
    n = []
    if num == 0:
        return 0

    while num > 0:
        n.append(num % 2)
        num //= 2

    return n[::-1]

deca = digit_to_Deca(N)
digits = deca_to_Digit(deca * 17)

for i in digits:
    print(i, end='')