a, b, c = map(int, input().split())

# Write your code here!

time1 = 11 * 24 * 60 + 11 * 60 + 11

time2 = a * 24 * 60 + b * 60 + c

answer = time2 - time1 if time2 - time1 > -1 else -1

print(answer)