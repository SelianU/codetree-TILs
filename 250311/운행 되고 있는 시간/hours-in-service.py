n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0

for i in range(n):
    count = 0
    working_time = [0] * 1000
    new_times = times[:i] + times[i + 1:]
    for time in new_times:
        for i in range(time[0], time[1]):
            working_time[i] += 1
    for work in working_time:
        if work > 0:
            count += 1
    answer = max(answer, count)

print(answer)