def get_list(str):
    str_list = str.split(" ")
    result_list = []
    for str in str_list:
        result_list.append(int(str))
    return result_list

n = int(input())
b_str = input()
b_list = get_list(b_str)

result = 0
pre_num = pow(10, 5)
for b in b_list:
    if b >= pre_num:
        result += pre_num
    else:
        result += b
    pre_num = b
result += b_list[-1]

print(result)


