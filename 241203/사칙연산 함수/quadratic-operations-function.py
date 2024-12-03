def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

sentence = input()

li = sentence.split()
li[0] = int(li[0])
li[2] = int(li[2])

if li[1] == "+": answer = add(li[0], li[2])
elif li[1] == "-": answer = sub(li[0], li[2])
elif li[1] == "*": answer = mul(li[0], li[2])
elif li[1] == "/": answer = div(li[0], li[2])
else:
    answer = False

if answer:
    print(f"{sentence} = {answer}")
else:
    print(answer)