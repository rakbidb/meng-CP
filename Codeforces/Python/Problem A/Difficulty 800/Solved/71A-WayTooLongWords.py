n = int(input())
for i in range(n):
    stringInput = input()
    if len(stringInput) > 10:
        print(stringInput[0] + str(len(stringInput) - 2) + stringInput[-1])
    else:
        print(stringInput)