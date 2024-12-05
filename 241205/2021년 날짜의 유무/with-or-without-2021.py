def exist(month, day):
    if month == 2:
        if day < 29:
            return True
        else:
            return False
    if month < 8:
        if month % 2 == 0 and day < 31:
            return True
        elif month % 2 == 1 and day < 32:
            return True
    elif month < 13:
        if month % 2 == 0 and day < 32:
            return True
        elif month % 2 == 1 and day < 31:
            return True
    return False

m, d = map(int, input().split())

if exist(m, d):
    print("Yes")
else:
    print("No")