n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Write your code here!

class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def print(self):
        print(f"{self.name} {self.height} {self.weight}")

people = []

for i in range(n):
    people.append(People(name[i], height[i], weight[i]))

people.sort(key=lambda x: x.height)

for i in range(n):
    people[i].print()