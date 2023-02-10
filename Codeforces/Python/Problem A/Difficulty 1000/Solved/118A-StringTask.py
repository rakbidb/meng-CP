a = []

stringInput = input().lower()
stringInput = stringInput.replace("a", "")
stringInput = stringInput.replace("o", "")
stringInput = stringInput.replace("y", "")
stringInput = stringInput.replace("e", "")
stringInput = stringInput.replace("u", "")
stringInput = stringInput.replace("i", "")
list_stringInput = list(stringInput)

for b in stringInput:
    c = "." + b
    a.append(c)
print("".join(a))