a, b, c = map(int, input().split())

# Write your code here!

time1 = 11 * 24 * 60 + 11 * 60 + 11

time2 = a * 24 * 60 + b * 60 + c

print(time2 - time1)