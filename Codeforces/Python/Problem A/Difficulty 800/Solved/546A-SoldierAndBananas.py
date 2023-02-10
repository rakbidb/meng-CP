k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)

x = k*(w*(w+1)/2)
if x <= n:
    print("0")
else:
    print(int(x - n))