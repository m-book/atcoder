import math

S = input()
K = int(input())

pre = ""
count = 0

if K >= 2:
    S += S
    K /= 2.0
for s in S:
    if s == pre:
        pre = ""
        count += 1
    else:
        pre = s

result = count * K

if S[0] == pre:
    result += (K-1)

print(math.floor(result))
