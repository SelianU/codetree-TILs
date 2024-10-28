li = list(map(int, input().split()))

for i in range(8):
    li.append(2*li[i]+li[i+1])
    print(li[i], end=' ')
print(f"{li[-2]} {li[-1]}")