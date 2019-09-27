S = input()
ok = True
for i, s in enumerate(S):
    index = i+1
    if index % 2 == 0 and s == "R":
        ok = False
        break
    if index % 2 == 1 and s == "L":
        ok = False
        break

if ok:
    print("Yes")
else:
    print("No")