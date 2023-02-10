upp = 0
low = 0

string = input()
for i in range(len(string)):
    x = string[i]
    if x.isupper() == True:
        upp += 1
    else:
        low += 1
if upp > low:
    print(string.upper())
else:
    print(string.lower())