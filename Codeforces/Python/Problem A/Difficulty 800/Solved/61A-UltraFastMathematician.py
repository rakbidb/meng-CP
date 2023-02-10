a = input()
b = input()
hasil = ""
for i in range(len(a)):
    if a[i] != b[i]:
        hasil += "1"
    else:
        hasil += "0"

print(hasil)