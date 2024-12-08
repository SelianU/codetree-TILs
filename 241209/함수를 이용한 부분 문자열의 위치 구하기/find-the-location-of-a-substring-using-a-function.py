def start(str1, str2):
    k = str1.find(str2)
    return k

str1 = input()
str2 = input()

if str2 in str1:
    print(start(str1, str2))
else:
    print(-1)