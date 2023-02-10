x = int(input())
count = 0
while x > 0:
    if x > 5:
        x -= 5
        count += 1
    else:
        count += 1
        x = 0

print(count)