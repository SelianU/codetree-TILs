b = input()

if '0' in b:
    idx = b.index('0')
    flipped = b[:idx] + '1' + b[idx+1:]
else:
    flipped = b[:-1] + '0'

print(int(flipped, 2))
