N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
차이 = float('inf')

for i in range(N):
    for j in range(i + 1, N):
        array = arr[:i] + arr[i + 1:j] + arr[j + 1:]
        if sum(array) - S < 차이:
            차이 = sum(array) - S

print(차이)