m1, d1, m2, d2 = map(int, input().split())
A = input()

# Write your code here!

months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}

day1 = d1
for i in range(m1):
    day1 += months[i]

day1 += day_of_week[A]

day2 = d2
for i in range(m2):
    day2 += months[i]

day = day2 - day1

answer = day // 7 + 1

print(answer)