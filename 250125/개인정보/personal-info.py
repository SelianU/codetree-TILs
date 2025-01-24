n = 5
name = []
height = []
weight = []

for _ in range(n):
    na, h, w = input().split()
    name.append(na)
    height.append(int(h))
    weight.append(float(w))

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

people.sort(key=lambda x: x.name)

print("name")
for i in range(n):
    people[i].print()

people.sort(key=lambda x: -x.height)
print("\nheight")
for i in range(n):
    people[i].print()