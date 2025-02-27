N = int(input())
numbers = list(map(int, input().split()))

answer = 0

for idx in range(len(numbers) - 2):
     for i in range(idx + 2, len(numbers)):
        answer = max(answer, numbers[idx] + numbers[i])

print(answer)