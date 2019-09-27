n = input()
nums_str = input()
num_str_list = nums_str.split(" ")
num_list = list(map(lambda x: int(x), num_str_list))
num_list.sort()

temp = num_list[0]
num_list.pop(0)
for num in num_list:
    temp += num
    temp /= 2

print(temp)
