t = int(input())
 
for _ in range(t):
    n = input()
    values = []
    counter = 0
    for i in range(len(n)):
        cur = int(n[i])
        if cur != 0:
            values.append(cur*10**(len(n)-i-1))
            counter+=1
    print(counter)
    print(" ".join([str(x) for x in values]))
