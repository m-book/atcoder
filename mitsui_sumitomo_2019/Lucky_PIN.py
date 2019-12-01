N = int(input())
S = input()

count = 0
count_dict = {}
for s in S:
    for k, v in count_dict.items():
        for k2, v2 in v.items():
            if s not in v2:
                v2.append(s)
                count += 1
        if s not in v.keys():
            v[s] = []
    if s not in count_dict.keys():
        count_dict[s] = {}

# print(count_dict)
print(count)
