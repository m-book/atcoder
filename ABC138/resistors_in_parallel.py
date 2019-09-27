import fractions

def get_lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def get_num(a, lcm):
    return lcm // a


N_str = input()
a_str = input()
a_str_list = a_str.split(" ")
a_list = list(map(lambda x: int(x), a_str_list))
lcm = 1
for a in a_list:
    lcm = get_lcm(lcm, a)

sum_a = 0
for a in a_list:
    sum_a += get_num(a, lcm)

result = lcm / sum_a
print(result)
