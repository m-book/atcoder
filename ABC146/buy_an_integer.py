abx = list(map(lambda x: int(x), input().split(" ")))
A = abx[0]
B = abx[1]
X = abx[2]

result = 0
first = True
for i in reversed(range(10)):
    if first:
        left = X - B * (i+1)
    else:
        left = X
    if left / A >= pow(10, i):
        for j in reversed(range(1, 10)):
            n = j * pow(10, i)
            if left / A >= n:
                result += n
                X -= A * n
                if first:
                    X -= B * (i+1)
                    first = False
                break
if result > 1000000000:
    result = 1000000000

print(result)
