n = int(input())
batu = input()
counter = 0

for i in range(1, n):
    if batu[i] == batu[i - 1]:
        counter += 1

print(counter)