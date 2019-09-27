A_B = input()
A_B_list = A_B.split(" ")

A = int(A_B_list[0])
B = int(A_B_list[1])

socket = 1
result = 0


# if A == 2:
#     print(B-1)
# else:
#     result = (B // (A - 1)) + 1
#     if (A-1) * (result-1) + 1 == B:
#         result -= 1
#
#     print(result)

while True:
    if socket >= B:
        print(result)
        break
    socket += (A-1)
    result += 1
