num = int(input())

num_range = range(1, 10)

flag = False

for n in reversed(num_range):
    if flag:
        break
    if num % n == 0:
        temp = num / n
        for m in num_range:
            if flag:
                break
            if temp == m:
                flag = True

if flag:
    print("Yes")
else:
    print("No")