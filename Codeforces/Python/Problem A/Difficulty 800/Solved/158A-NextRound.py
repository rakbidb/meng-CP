count = 0
 
n, k = input().split()
 
a = list(map(int, input().split()))
if max(a) != 0:
    for i in range(int(n)):
        if a[int(k)-1] <= a[i] and a[i] != 0:
            count += 1
 
print(count)