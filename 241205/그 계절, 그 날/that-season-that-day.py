def yoonyear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def check_date(year, month):
    if month == 2:
        if yoonyear(year):
            return 29
        else:
            return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31

def date_exist(year, month, day):
    if day <= check_date(year, month):
        return True
    return False

def check_season(year, month, day):
    if date_exist(year, month, day):
        if month == 3 or month == 4 or month == 5:
            return 1
        elif month == 6 or month == 7 or month == 8:
            return 2
        elif month == 9 or month == 10 or month == 11:
            return 3
        elif month == 12 or month == 1 or month == 2:
            return 4
    return -1


y, m, d = map(int, input().split())

season = check_season(y, m, d)

if season == 1:
    print("Spring")
elif season == 2:
    print("Summer")
elif season == 3:
    print("Fall")
elif season == 4:
    print("Winter")
else:
    print(-1)
