def yoon_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

year = int(input())

if yoon_year(year):
    print("true")
else:
    print('false')