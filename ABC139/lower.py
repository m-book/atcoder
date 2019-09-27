N = input()
num_str = input()
num_str_list = num_str.split(" ")

result = 0
temp_result = 0

pre_num = int(num_str_list.pop(0))

for num_str in num_str_list:
    num = int(num_str)
    if num > pre_num:
        if result < temp_result:
            result = temp_result
        temp_result = 0
    else:
        temp_result += 1
    pre_num = num

if result < temp_result:
    result = temp_result

print(result)
