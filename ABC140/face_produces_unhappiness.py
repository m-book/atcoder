n_k_str = input()
n_k_list = n_k_str.split(" ")
N = int(n_k_list[0])
K = int(n_k_list[1])
S = list(input())

pre_s = S.pop(0)
pre_index = -1
result = 0
for i,s in enumerate(S):
    if s != pre_s:
        temp = i - pre_index - 1
        result += temp
        pre_index = i
    pre_s = s

temp = len(S) - pre_index - 1
result += temp

result += K*2
if result >= N:
    result = N - 1

print(result)
