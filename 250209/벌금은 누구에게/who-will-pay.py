N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Write your code here!
students = {}
answer = -1

for i in range(M):
    if student[i] not in students.keys():
        students[student[i]] = 1
    else:
        students[student[i]] += 1

for key, value in students.items():
    if value >= K:
        answer = key
        break

print(answer)