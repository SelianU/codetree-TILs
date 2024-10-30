n = int(input())

li = [input() for _ in range(n)]

c = input()

count = 0
gkq = 0

for k in li:
    if c == k[0]:
        count += 1
        gkq += len(k)

avg = gkq/count

print(f"{count} {avg:.2f}")