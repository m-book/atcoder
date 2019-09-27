from collections import defaultdict


class Node:
    def __init__(self):
        self.num = 0
        self.node_list = []

    def add(self, add_num):
        self.num += add_num
        for node in self.node_list:
            node.add(add_num)

setting_str = input()
setting_str_list = setting_str.split(" ")
N = int(setting_str_list[0])
Q = int(setting_str_list[1])
node_dict = {}
for i in range(1, N+1):
    node_dict[i] = Node()

for i in range(N-1):
    num_str  = input()
    num_str_list = num_str.split(" ")
    a = int(num_str_list[0])
    b = int(num_str_list[1])
    node_dict[a].node_list.append(node_dict[b])

add_dict = defaultdict(int)
for i in range(Q):
    num_str = input()
    num_str_list = num_str.split(" ")
    a = int(num_str_list[0])
    b = int(num_str_list[1])
    add_dict[a] += b

for k, v in add_dict.items():
    node_dict[k].add(v)

result = ""
for node in node_dict.values():
    result += str(node.num) + " "
result = result[:-1]
print(result)
