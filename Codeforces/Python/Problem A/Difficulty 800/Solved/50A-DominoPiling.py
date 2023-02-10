M, N = input().split()
M = int(M)
N = int(N)

if (M * N) % 2 == 0:
    print(int((M * N)/2))
if (M * N) % 2 == 1:
    print(int((M * N)//2))