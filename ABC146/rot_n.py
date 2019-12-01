chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = int(input())
S = input()

result = ""
for s in S:
    index = chars.index(s)
    index = (index + N) % 26
    result += chars[index]

print(result)