n_k_str = input()
n_k = n_k_str.split(" ")
N = int(n_k[0])
K = int(n_k[1])
p_str = input()
p_list = p_str.split(" ")
p_list = list(map(int, p_list))

max_num = p_list[K-1]

index = K
result = 1
while True:
    print(max_num)
    if index >= N:
        break
    if p_list[index] < max_num:
        result += 1
    max_num = p_list[index]
    index += 1


print(result)
