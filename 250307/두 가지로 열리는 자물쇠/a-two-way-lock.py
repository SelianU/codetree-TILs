N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
def mod(n, m):
    return n % m

def overlap():
    a = b = c = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            if mod(a1 + i, N) == mod(a2 + j, N):
                a += 1
            if mod(b1 + i, N) == mod(b2 + j, N):
                b += 1
            if mod(c1 + i, N) == mod(c2 + j, N):
                c += 1
    return a * b * c

if N < 5:
    answer = N * N * N
else:
    answer = 250 - overlap()

print(answer)