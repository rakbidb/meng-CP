l = int(input())
while l > 0:
    a, b = map(int, input().split())
    print((abs(a - b) + 9) // 10)
    l -= 1