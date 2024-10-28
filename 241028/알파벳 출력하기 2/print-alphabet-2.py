n = int(input())
k = ord('A')
for i in range(n):
    print(' ' * 2 * i, end='')
    for j in range(n - i):
        print(chr(k), end=' ')
        k += 1
        if k == 91:
            k = 65
    print()