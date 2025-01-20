n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Write your code here!
class Street:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region
    
    def print(self):
        print(f"name {self.name}\naddr {self.street_address}\ncity {self.region}")

streets = []

for i in range(n):
    street = Street(name[i], street_address[i], region[i])
    streets.append(street)

slow_name = 0

for i in range(1, n):
    if streets[slow_name].name < streets[i].name:
        slow_name = i

streets[slow_name].print()