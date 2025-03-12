N, M, D, S = map(int, input().split())

eat_cheese = [tuple(map(int, input().split())) for _ in range(D)]
sick = [tuple(map(int, input().split())) for _ in range(S)]

possible_sick_cheese = []

# 아픈 시간 이전에 먹은 치즈 확인
for sick_person in sick:
    for cheese_person in eat_cheese:
        if cheese_person[0] == sick_person[0] and cheese_person[2] < sick_person[1]:
            possible_sick_cheese.append((cheese_person[0], cheese_person[1]))

# 모든 아픈 사람에 중복되는 치즈만 걸러냄
sick_cheese = []
count = 0
if len(possible_sick_cheese) == 1:
    sick_cheese = [possible_sick_cheese[0][1]]
else:
    for i in range(len(possible_sick_cheese)):
        # 1번은 같은게 s개 있으면 가능성 있음
        for j in range(i, len(possible_sick_cheese)):
            if possible_sick_cheese[i][1] == possible_sick_cheese[j][1]:
                count += 1
        if count > S:
            sick_cheese.append(possible_sick_cheese[i][1])

sick_cheese = set(sick_cheese)

# print(possible_sick_cheese)
# print(sick_cheese)

answer = 0
for cheese in sick_cheese:
    sick_person = []
    for cheese_person in eat_cheese:
        if cheese_person[1] == cheese:
            sick_person.append(cheese_person[0])
    answer = max(answer, len(set(sick_person)))

print(answer)