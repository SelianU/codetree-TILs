def palindrome(str_):
    return str_[::-1]

a = input()

str_ = palindrome(a)

if a == str_:
    print("Yes")
else:
    print("No")