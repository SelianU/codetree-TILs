n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Write your code here!
# class Student:
#     def __init__(self, height, weight, number):
#         self.height = height
#         self.weight = weight
#         self.number = number

students.sort(key=lambda x: (x[0], -x[1]))

for i in  range(n):
    print(f"{students[i][0]} {students[i][1]} {students[i][2]}")