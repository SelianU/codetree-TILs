m1, d1, m2, d2 = map(int, input().split())

# Write your code here!

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day1 = d1
for i in range(m1):
    day1 += months[i]

day2 = d2
for i in range(m2):
    day2 += months[i]

day = day2 - day1
dow = day_of_week[day % 7]

print(dow)