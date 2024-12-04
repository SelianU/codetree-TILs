def continuous_partial_sequence(parent_li, child_li, parent_size, child_size):
    k = 0
    for i in range(parent_size):
        if parent_li[i] == child_li[k]:
            k += 1
            if k == child_size:
                break
            else:
                continue
        if k != 0:
            return False
    if k == child_size:
        return True
    else:
        return False
        

li_a_size, li_b_size = map(int, input().split())

li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))

if continuous_partial_sequence(li_a, li_b, li_a_size, li_b_size):
    print("Yes")
else:
    print("No")