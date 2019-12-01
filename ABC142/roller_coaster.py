n_k = input().split(" ")
N = int(n_k[0])
K = int(n_k[1])

heights = input().split(" ")
result = 0
for h in heights:
    if int(h) >= K:
        result += 1

print(result)
