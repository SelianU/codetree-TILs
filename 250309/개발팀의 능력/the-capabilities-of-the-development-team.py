arr = list(map(int, input().split()))

# Please write your code here.
min_difference = float('inf')

for i in range(5):
    team1 = arr[i]
    for j in range(5):
        if i != j:
            for k in range(5):
                if i != k and j != k and k != i:
                    team2 = arr[j] + arr[k]
                    team3 = sum(arr) - team1 - team2
                    if team1 != team2 and team2 != team3 and team3 != team1:
                        min_difference = min(min_difference, max(team1, team2, team3) - min(team1, team2, team3))

if min_difference == float('inf'):
    min_difference = -1

print(min_difference)