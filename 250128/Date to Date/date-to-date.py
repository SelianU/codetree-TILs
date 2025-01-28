m1, d1, m2, d2 = map(int, input().split())

# Write your code here!
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

first, second = 0, 0

for i in range(m1 + 1):
    first += months[i]
first += d1

for i in  range(m2 + 1):
    second += months[i]
second += d2

print(second - first)