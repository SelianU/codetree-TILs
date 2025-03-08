ability = list(map(int, input().split()))

# Please write your code here.
ability.sort()

team1 = ability[0] + ability[-1]
team2 = ability[1] + ability[-2]
team3 = ability[2] + ability[-3]

answer = (team1, team2, team3)

print(max(answer) - min(answer))