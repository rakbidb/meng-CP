n = input().split()
panjang = int(n[0])
lebar = int(n[1])
ubin = int(n[2])
if panjang % ubin == 0 and lebar % ubin == 0:
	a = panjang // ubin
	b = lebar // ubin
elif panjang % ubin == 0 and lebar % ubin != 0:
	a = panjang // ubin
	b = (lebar // ubin) + 1
elif panjang % ubin != 0 and lebar % ubin == 0:
	a = (panjang // ubin) + 1
	b = lebar // ubin
elif panjang % ubin != 0 and lebar % ubin != 0:
	a = (panjang // ubin) + 1
	b = (lebar // ubin) + 1
print(a * b)