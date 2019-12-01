N = int(input())
As = list(map(lambda x: int(x), input().split(" ")))

hat_list = [0] * 100000

result = 1

for a in As:
    pre_hat = hat_list[a-1]
    if a == 0:
        pre_hat = 3
    hat = hat_list[a]

    result *= (pre_hat - hat)
    result %= 1000000007
    hat_list[a] += 1

print(result)
