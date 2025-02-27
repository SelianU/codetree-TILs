N = int(input())
numbers = [input() for _ in range(N)]

non_carry_numbers = 0
count = 0

def maxlen(num1, num2, num3):
    return max(len(num1), len(num2), len(num3))

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            m = maxlen(numbers[i], numbers[j], numbers[k])
            num1, num2, num3 = map(int, (numbers[i], numbers[j], numbers[k]))
            p = 0
            for power in range(m):
                if (num1 // (10 ** power)) % 10 + (num2 // (10 ** power)) % 10 + (num3 // (10 ** power)) % 10 > 9:
                    break
                p += 1
            if p == m:
                non_carry_numbers = max(non_carry_numbers, num1 + num2 + num3)
                count += 1

if count == N * (N - 1) * (N - 2):
    print(-1)
else:
    print(non_carry_numbers)