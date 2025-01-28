m1, d1, m2, d2 = map(int, input().split())

# Write your code here!
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

first, second = d1, d2 + 1

for i in range(m1):
    first += months[i]

for i in  range(m2):
    second += months[i]

answer = second - first

print(answer)