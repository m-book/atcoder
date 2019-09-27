import math
n_m_str = input()
n_m = n_m_str.split(" ")
N = int(n_m[0])
M = int(n_m[1])

a_str = input()
a_s = a_str.split(" ")
a_list = []
for a in a_s:
    a_list.append(int(a))
for i in range(M):
    index = a_list.index(max(a_list))
    a_list[index] /= 2
sum = 0
for i in a_list:
    sum += math.floor(i)
print(sum)