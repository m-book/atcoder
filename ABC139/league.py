N = int(input())

team_dict = {}
for i in range(N):
    temp_str = input()
    temp_list = temp_str.split(" ")
    mapped_list = list(map(lambda x: int(x), temp_list))
    team_dict[i+1] = mapped_list

result = 0
empty_list_count = 0

while True:
    if empty_list_count == N:
        break
    delete_list = []
    for i in range(N):
        index = i + 1
        try:
            pear_index =  team_dict[index][0]
        except:
            continue
        if index == team_dict[pear_index][0]:
            delete_list.append(index)
    if len(delete_list) == 0:
        break
    result += 1
    for i in delete_list:
        team_dict[i].pop(0)
        if len(team_dict[i]) == 0:
            empty_list_count += 1

if empty_list_count == N:
    print(result)
else:
    print(-1)
