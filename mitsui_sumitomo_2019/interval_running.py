Ts = list(map(lambda x: int(x), input().split(" ")))
As = list(map(lambda x: int(x), input().split(" ")))
Bs = list(map(lambda x: int(x), input().split(" ")))

t1 = Ts[0]
t2 = Ts[1]
a1 = As[0]
a2 = As[1]
b1 = Bs[0]
b2 = Bs[1]

result = 0
difference = 0

if t1 * a1 + t2 * a2 == t1 * b1 + t2 * b2:
    print("infinity")
else:
    while True:
        difference += t1*(a1-b1)

        if result > 0:
            if a1-b1 > 0 and difference <= 0:
                break
            elif a1-b1 < 0 and difference >= 0:
                break
        result += 1

        difference += t2*(a2-b2)

        if result > 0:
            if a2-b2 > 0 and difference <= 0:
                break
            elif a2-b2 < 0 and difference >= 0:
                break
        result += 1

    print(result-1)
