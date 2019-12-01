X = int(input())

x = X % 100
count = X // 100

for i in range(count):
    if x >= 5:
        x -= 5
    else:
        x = 0

if x == 0:
    print(1)
else:
    print(0)
