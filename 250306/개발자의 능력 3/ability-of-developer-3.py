abilities = list(map(int, input().split()))

# Please write your code here.
answer = float('inf')

for i in range(6):
    for j in range(6):
        for k in range(6):
            sum1 = abilities[i] + abilities[j] + abilities[k]
            sum2 = sum(abilities) - sum1
            answer = min(abs(sum2 - sum1), answer)
print(answer)