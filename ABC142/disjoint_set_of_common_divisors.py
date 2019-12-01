a_b = input().split(" ")
A = int(a_b[0])
B = int(a_b[1])

p_nums = []
for i in range(1, int(max([A, B])**0.5) + 1):
    is_p_num = True
    if A % i == 0 and B % i == 0:
        for p in p_nums:
            if p == 1:
                continue
            if i % p == 0:
                is_p_num = False
                break
        if is_p_num:
            p_nums.append(i)

print(len(p_nums))