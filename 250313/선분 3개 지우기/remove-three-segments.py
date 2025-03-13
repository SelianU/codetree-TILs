n = int(input())

lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            t_lines = [0] * 100
            new_lines = lines[:i] + lines[i + 1:j] + lines[j + 1:k] + lines[k + 1:]
            for line in new_lines:
                for l in range(line[0], line[1] + 1):
                    t_lines[l] += 1
            if max(t_lines) == 1:
                answer += 1

print(answer)