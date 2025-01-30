N, B = map(int, input().split())

# Write your code here!
answer = []

while N > 0:
    answer.append(N % B)
    N //= B

for i in answer[::-1]:
    print(i, end='')