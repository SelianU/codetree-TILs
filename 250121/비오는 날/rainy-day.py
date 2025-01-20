n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Write your code here!
class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

    def print(self):
        print(f"{self.date} {self.day} {self.weather}")

weathers = []

for i in range(n):
    weathers.append(Weather(date[i], day[i], weather[i]))

for i in range(n):
    if weathers[i].weather == "Rain":
        rainy = i
        break

for i in range(n):
    if weathers[rainy].date > weathers[i].date and weathers[i].weather == "Rain":
        rainy = i

weathers[rainy].print()