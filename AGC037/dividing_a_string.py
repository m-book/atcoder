string = input()
temp = ""
last = ""
count = 0
for s in string:
    if temp=="":
        temp=s
    elif temp==last:
        temp+=s
    else:
        last=temp
        temp=s
        count+=1

if temp != "" and temp != last:
    count += 1

print(count)


s=input()
temp_new=""
temp_old=""
cnt=0
for i in range(len(s)):
    if temp_new=="":
        temp_new=s[i]
    elif temp_new==temp_old:
        temp_new+=s[i]
    else:
        temp_old=temp_new
        temp_new=s[i]
        cnt+=1
if temp_new!=temp_old and temp_new!="":
    cnt+=1