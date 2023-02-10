count = 0
n = str(int(input()))
for i in n:
    if i == "4" or i == "7":
        count += 1

if count == 4:
    print("YES")
elif count == 7:
    print("YES")
else: 
    print("NO")