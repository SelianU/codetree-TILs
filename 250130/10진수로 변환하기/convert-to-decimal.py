binary = input()

# Write your code here!
num = 0

for i, j in enumerate(binary[::-1]):
    num += (2 ** i) * int(j)

print(num)