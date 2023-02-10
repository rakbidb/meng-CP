a = input()
b = int(a) + 1
count = True
while count:
	c = set(str(b))
	if len(c) < len(str(b)):
		b += 1
	else:
		count = False
print(b)