N, M, D, S = map(int, input().split())

eat_cheese = [tuple(map(int, input().split())) for _ in range(D)]
sick = [tuple(map(int, input().split())) for _ in range(S)]

# Please write your code here.

# n명 m개 치즈 d개의 기록 s개의 아픈기록, 다른 사람도 아플 수 있음

# d개의 치즈 먹은 기록
# (p 번째 사람, m번째 치즈, t초에 먹음)

# s개의 아픈 기록
# (p번째 사람, t초에 아픔)

possible_sick_cheese = []

# 시간 순에 따라 정렬
eat_cheese.sort(key=lambda x:x[2])
sick.sort(key=lambda x:x[1])

# 아픈 시간 이전에 먹은 치즈 확인
for sick_person in sick:
    for cheese_person in eat_cheese:
        if cheese_person[0] == sick_person[0] and cheese_person[2] < sick_person[1]:
            possible_sick_cheese.append((cheese_person[0], cheese_person[1]))

# 모든 아픈 사람에 중복되는 치즈만 걸러냄
sick_cheese = []
count = 0
for i in range(len(possible_sick_cheese)):
    # 1번은 같은데 0번이 다른게 s개 있으면 가능성 있음
    for j in range(i + 1, len(possible_sick_cheese)):
        if possible_sick_cheese[i][1] == possible_sick_cheese[j][1] and possible_sick_cheese[i][0] != possible_sick_cheese[j][0]:
            count += 1
    if count == S:
        sick_cheese.append(possible_sick_cheese[i][1])

sick_cheese = set(sick_cheese)

sick_person = []
answer = 0
for cheese_person in eat_cheese:
    if cheese_person[1] in sick_cheese:
        sick_person.append(cheese_person[0])

print(len(set(sick_person)))

# 아픈 사람의 시간을 받고
# 그 사람이 아픈 시간 이전에 시간에 먹은 치즈를 확인하고
# 그 치즈를 먹은 사람은 다 아프다고 가정