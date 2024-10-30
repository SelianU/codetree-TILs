str1 = input()
str2 = input()
str3 = input()

answer = abs(len(str1)-len(str2))
answer = max(answer, abs(len(str1)-len(str3)))
answer = max(answer, abs(len(str2)-len(str3)))

print(answer)