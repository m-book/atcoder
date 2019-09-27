def get_list(str):
    str_list = str.split(" ")
    result_list = []
    for str in str_list:
        result_list.append(int(str))
    return result_list

n = int(input())
num_str = input()
num_list = get_list(num_str)

result = 0
max_num = 0
second_num = 0

for n in num_list:
    if n > max_num:
        second_num = max_num
        max_num = n
    elif n > second_num:
        second_num = n
    result += second_num

while True:
    max_num = 0
    second_num = 0
    num_list.pop(0)
    if len(num_list) < 2:
        break
    num_list = list(reversed(num_list))
    for n in num_list:
        if n > max_num:
            second_num = max_num
            max_num = n
        elif n > second_num:
            second_num = n
        result += second_num

print(result)