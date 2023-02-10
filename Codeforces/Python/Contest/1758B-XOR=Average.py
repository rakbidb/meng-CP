# print(5 & 7) --> operator XOR
t = int(input())
for i in range(t):
    n = input()
    if n == 2:
        print(1 + " " + 3)
    elif (n & 1) == 1:
        while i <= n:
            print(1 + " ")
            i += 1
    else:
        print(1 + " " + 2 + " " + 3 + " ")
        while i <= n:
            print(2 + " ")