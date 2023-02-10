n = int(input())
p = list(map(int, input().split()))[:n]
x = 100 / n
persentase = 0
for i in p:
    if i != 0:
        persentase += x / (100 / i)
print(persentase)