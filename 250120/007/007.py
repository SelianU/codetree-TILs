secret_code, meeting_point, time = input().split()
time = int(time)

# Write your code here!

class Spy:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

    def print(self):
        print(f"secret code : {self.secret_code}")
        print(f"meeting point : {self.meeting_point}")
        print(f"time : {self.time}")

spy1 = Spy(secret_code, meeting_point, time)

spy1.print()