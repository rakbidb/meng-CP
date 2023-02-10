x = []
for a in range(0, 5):
	x.append(input().split(" "))
for i in range(0,5):
	for j in range(0, 5):
		if x[i][j] == "1":
			baris = i + 1
			kolom = j + 1
print(abs(baris -3) + abs(kolom - 3))