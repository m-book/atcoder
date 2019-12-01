N = int(input())

if N % 2 == 1:
    print("No")
else:
    S = input()
    threshold = N//2
    front = S[:threshold]
    back = S[threshold:]
    if front == back:
        print("Yes")
    else:
        print("No")

