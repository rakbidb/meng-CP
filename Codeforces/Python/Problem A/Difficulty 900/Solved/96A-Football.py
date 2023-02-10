dangerous_counter = 0
condition = True

stringInput = input()
list_stringInput = list(stringInput)

for i in range(0, len(stringInput) - 1):
    if list_stringInput[i] == list_stringInput[i + 1]:
        dangerous_counter += 1
    else:
        dangerous_counter = 0

    if dangerous_counter == 6:
        condition = False
        break     

if condition:
    print("NO")
else: 
    print("YES")