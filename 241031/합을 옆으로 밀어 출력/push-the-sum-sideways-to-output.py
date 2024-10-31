n = int(input())

answer = str(sum([int(input()) for _ in range(n)]))
answer = answer[1:]+answer[0]

print(answer)