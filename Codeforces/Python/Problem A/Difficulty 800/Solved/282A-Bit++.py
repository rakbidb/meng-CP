x = 0
n = int(input())
for i in range(0,n):
    stringInput = input()
    if "+" in stringInput:
        x += 1
    elif "-" in stringInput: 
        x -= 1

print(x)