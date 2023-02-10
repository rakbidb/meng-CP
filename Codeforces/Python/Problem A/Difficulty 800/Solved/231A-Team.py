count = 0

n = int(input())
for i in range(0,n):
    a, b, c = input().split()
    if int(a) + int(b) + int(c) >= 2:
        count += 1
    else: 
        continue

print(count)