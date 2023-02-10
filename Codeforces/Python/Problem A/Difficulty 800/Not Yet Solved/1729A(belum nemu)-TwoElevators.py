t = int(input())
x, y, z = map(int, input().split())

ta = abs(x - 1)
tb = abs(y - z) + abs(z - 1)

if ta == tb:
    print("3")
elif ta < tb:
    print("2")
    