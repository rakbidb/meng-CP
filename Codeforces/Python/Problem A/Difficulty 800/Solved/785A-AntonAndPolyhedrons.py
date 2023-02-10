n = int(input())
hasil = 0

for i in range(n):
    string = input()
    if string == "Tetrahedron":
        hasil += 4
    elif string == "Cube":
        hasil += 6
    elif string == "Octahedron":
        hasil += 8
    elif string == "Dodecahedron":
        hasil += 12
    elif string == "Icosahedron":
        hasil += 20

print(hasil)