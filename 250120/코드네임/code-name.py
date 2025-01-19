MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Write your code here!

class Codename:
    def __init__(self, codenames = [], scores = []):
        self.codenames = codenames
        self.scores = scores

    def print(self):
        for i in range(len(self.codenames)):
            print(f"{self.codenames[i]} {self.scores[i]}")

    def min_code(self):
        temp = self.scores[0]
        temp2 = self.codenames[0]
        for i in range(1, len(self.codenames)):
            if self.scores[i] < temp:
                temp = self.scores[i]
                temp2 = self.codenames[i]
        return temp2, temp

    def print_min(self):
        codename, score = self.min_code()
        print(f"{codename} {score}")

code = Codename(codenames, scores)

code.print_min()