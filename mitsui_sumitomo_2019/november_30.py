today = input()
tomorrow = list(map(lambda x: int(x), input().split(" ")))

if tomorrow[1] == 1:
    print(1)
else:
    print(0)
