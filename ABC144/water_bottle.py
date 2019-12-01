import math

nums = list(map(int, input().split(" ")))

a = nums[0]
b = nums[1]
x = nums[2]

bottle = a * a * b

if bottle / 2.0 < x:
    temp = bottle - x
    y = temp * 2 / a / a
    result = math.degrees(math.atan(y/a))
else:
    y = x * 2 / b / a
    result = math.degrees(math.atan(b/y))

print(result)
