_sum, avg = 0, 0

while True:
    age = int(input())
    if not 19 < age < 30:
        break
    _sum += age
    avg += 1

avg = _sum / avg

print(f"{avg:.2f}")