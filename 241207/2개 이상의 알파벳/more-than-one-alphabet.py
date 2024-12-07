def different(str_):
    m = str_[0]
    for i in range(1, len(str_)):
        if m != i:
            return True
    return False

a = input()

if different(a):
    print("Yes")
else:
    print("No")