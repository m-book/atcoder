num_str = input()
result = input()
try:
    num = int(num_str)
except:
    print("not num")
    exit()
if num < 3200:
    result = "red"
print(result)
