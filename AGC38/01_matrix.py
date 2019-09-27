def concat_list(l):
    maped_list = map(str, l)
    return "".join(maped_list)

condition = input()
condition_list = condition.split(" ")
H = int(condition_list[0])
W = int(condition_list[1])
A = int(condition_list[2])
B = int(condition_list[3])

if A == 0 and B == 0:
    for i in range(H):
        temp_list = [0] * W
        print(concat_list(temp_list))
elif A == 0:
    count = 0
    for i in range(H):
        if count >= B:
            temp_list = [0] * W
        else:
            temp_list = [1] * W
            count += 1
        print(concat_list(temp_list))
elif B == 0:
    for i in range(H):
        temp_list = [0] * W
        add_index = 0
        while True:
            temp_list[add_index] = 1
            add_index += 1
            if add_index >= A:
                print(concat_list(temp_list))
                break
elif A*H != B*W:
    print("No")
else:
    start_index = 0
    count_list = [0] * W
    for i in range(H):
        temp_list = [0] * W
        add_index = 0
        while True:
            if count_list[start_index+add_index] >= B:
                start_index += 1
            else:
                count_list[start_index+add_index] += 1
                temp_list[start_index+add_index] = 1
                add_index += 1
                if add_index >= A:
                    print(concat_list(temp_list))
                    break
