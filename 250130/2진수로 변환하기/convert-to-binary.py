n = int(input())

# Write your code here!
digits = []

while n > 0:
    digits.append(n % 2)
    n //= 2

for digit in digits[::-1]:
    print(digit, end='')