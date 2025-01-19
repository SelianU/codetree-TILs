unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Write your code here!

class Cancel:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds
    
    def print(self):
        print(f"code : {self.unlock_code}")
        print(f"color : {self.wire_color}")
        print(f"second : {self.seconds}")

cancel = Cancel(unlock_code, wire_color, seconds)

cancel.print()