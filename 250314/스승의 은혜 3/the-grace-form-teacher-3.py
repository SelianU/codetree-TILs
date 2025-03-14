N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
answer = 0
for i in range(N):
    new_gifts = gifts[:i] + [(gifts[i][0] // 2, gifts[i][1])] + gifts[i + 1:]
    new_new_gifts = [sum(gift) for gift in new_gifts]
    new_new_gifts.sort()
    total = 0
    for j in range(len(new_new_gifts)):
        total += new_new_gifts[j]
        if total > B:
            answer = j + 1
            break

print(answer)