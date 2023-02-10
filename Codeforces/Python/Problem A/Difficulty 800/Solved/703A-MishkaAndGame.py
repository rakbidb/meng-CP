n = int(input())
mishka = 0
chris = 0

for i in range(n):
    m, c = map(int, input().split())
    if m < c:
        chris += 1
    elif m == c:
        chris += 0
        mishka += 0
    elif m > c:
        mishka += 1
if mishka > chris:
    print("Mishka")
elif mishka == chris:
    print("Friendship is magic!^^")
else:
    print("Chris")
