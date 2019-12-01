nums = list(map(int, input().split(" ")))
k = nums[1]
As = list(map(int, input().split(" ")))
Fs = list(map(int, input().split(" ")))

# dic = {}
#
# for i in range(len(As)):
#     dic[i] = [As[i], Fs[i], As[i] * Fs[i]]
#
# for _ in range(k):
#     key = max(dic.items(), key = lambda x:x[1][2])[0]
#     if dic[key][2] - dic[key][1] >= 0:
#         dic[key][2] -= dic[key][1]
#     print(dic[key][2])
#
# result = 0
# for v in dic.values():
#     result += v[2]
#
# print(result)

for i in range(k):
    index = As.index(max(As))
    if As[index] == 0:
        break
    As[index] -= 1

As.sort()
Fs.sort(reverse=True)


result = 0
for i in range(len(As)):
    result += As[i] * Fs[i]

print(result)
