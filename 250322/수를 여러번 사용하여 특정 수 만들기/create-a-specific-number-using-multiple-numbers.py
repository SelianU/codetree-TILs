A, B, C = map(int, input().split())

# Please write your code here.
a_count = C // A
b_count = 0

max_number = sum_of_number = a_count * A

while a_count >= 0:
    sum_of_number = A * a_count + B * b_count
    if sum_of_number <= C:
        max_number = max(max_number, sum_of_number)
        b_count += 1
    else:
        a_count -= 1

print(max_number)