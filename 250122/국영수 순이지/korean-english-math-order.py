n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Write your code here!

class Score:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def print(self):
        print(f"{self.name} {self.korean} {self.english} {self.math}")

scores = []

for i in range(n):
    scores.append(Score(name[i], korean[i], english[i], math[i]))

scores.sort(key=lambda x: (-x.korean, -x.english, -x.math))

for i in range(n):
    scores[i].print()