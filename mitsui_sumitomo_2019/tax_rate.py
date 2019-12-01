import math


N = int(input())

for i in range(1, 50001):
    num = math.floor(i * 1.08)
    if N == num:
        print(i)
        break
    elif num > N:
        print(":(")
        break
