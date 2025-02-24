b = input()

bi = int(b)

binarys = []

def to_digit(binary):
    re = 0
    i = 0
    while binary != 0:
        re += 2 ** i * (binary % 10)
        binary //= 10
        i += 1
    return re

for i in range(len(b)):
    if b[i] == '0':
        bi += 10 ** (len(b) - i - 1)
        binarys.append(bi)
        bi -= 10 ** (len(b) - i - 1)
    else:
        bi -= 10 ** (len(b) - i - 1)
        binarys.append(bi)
        bi += 10 ** (len(b) - i - 1)

max_num = 0

for binary in binarys:
    max_num = max(max_num, to_digit(binary))

print(max_num)