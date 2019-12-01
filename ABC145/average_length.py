import itertools

N = int(input())

towns = []
for i in range(N):
    town = list(map(lambda x: int(x), input().split(" ")))
    towns.append(town)

p = list(itertools.permutations(towns))
result = 0
for nums in p:
    pre = None
    for num in nums:
        if pre is None:
            pre = num
            continue
        x = pow(pre[0] - num[0], 2)
        y = pow(pre[1] - num[1], 2)
        result += pow(x+y, 0.5)
        pre = num

result /= len(p)
print(result)
